#!/usr/bin/python3
# coding=utf8

import sys
import cv2
import time
import math
import threading
import numpy as np
import yaml
from enum import Enum
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from puppy_control_msgs.msg import Velocity, Pose, Gait
from puppy_control_msgs.srv import SetRunActionName
from cv_bridge import CvBridge
import asyncio

ROS_NODE_NAME = 'negotiate_stairs_demo'

is_shutdown = False
lock = threading.Lock()
debug = False
__isRunning = True
haved_detect = False

class PuppyStatus(Enum):
    LOOKING_FOR = 0  # 寻找台阶
    FOUND_TARGET = 3  # 已经发现台阶目标
    DOWN_STAIRS = 4  # 下台阶
    STOP = 10
    END = 20

puppyStatus = PuppyStatus.LOOKING_FOR
puppyStatusLast = PuppyStatus.END

target_centre_point = None  # 目标中心点坐标

class PuppyStairClimbing(Node):
    def __init__(self):
        super().__init__(ROS_NODE_NAME)

        self.bridge = CvBridge()

        # 获取 PuppyPose 和 GaitConfig 参数
        pose_params = [
            'PuppyPose_LookDown_10deg_height',
            'PuppyPose_LookDown_10deg_pitch',
            'PuppyPose_LookDown_10deg_roll',
            'PuppyPose_LookDown_10deg_stance_x',
            'PuppyPose_LookDown_10deg_stance_y',
            'PuppyPose_LookDown_10deg_x_shift',
            'PuppyPose_LookDown_10deg_yaw'
        ]

        # 从参数服务器获取 PuppyPose 和 GaitConfig
        self.PuppyPose = self.get_parameters_from_server(pose_params)
        if not self.check_parameter_values(self.PuppyPose, pose_params):
            self.get_logger().error('Missing necessary PuppyPose parameters.')
            return

        # 从本地文件获取颜色参数
        self.color_range_list = self.get_color_ranges()
        if not self.color_range_list:
            self.get_logger().error('Failed to load color ranges from local file.')

        # 获取 GaitConfig 参数
        gait_params = [
            'GaitConfigFast_overlap_time',
            'GaitConfigFast_swing_time',
            'GaitConfigFast_clearance_time',
            'GaitConfigFast_z_clearance'
        ]
        self.GaitConfig = self.get_parameters_from_server(gait_params)
        if not self.check_parameter_values(self.GaitConfig, gait_params):
            self.get_logger().error('Missing necessary GaitConfig parameters.')
            return

        # 订阅图像话题，创建Publisher和Service客户端
        self.image_sub = self.create_subscription(Image, '/image_raw', self.image_callback, 10)
        self.PuppyGaitConfigPub = self.create_publisher(Gait, '/puppy_control/gait', 10)
        self.PuppyVelocityPub = self.create_publisher(Velocity, '/puppy_control/velocity', 10)
        self.PuppyPosePub = self.create_publisher(Pose, '/puppy_control/pose', 10)
        self.runActionGroup_srv = self.create_client(SetRunActionName, '/puppy_control/runActionGroup')

        while not self.runActionGroup_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for runActionGroup service...')

        self.publish_initial_pose_and_gait()

        self.is_shutdown = False
        th = threading.Thread(target=self.move)
        th.daemon = True
        th.start()

    def get_color_ranges(self):
        """从本地配置文件获取颜色范围列表"""
        try:
            with open('/home/ubuntu/software/lab_tool/lab_config.yaml', 'r') as file:
                config = yaml.safe_load(file)
                color_ranges = config.get('color_range_list', {})
                return color_ranges
        except Exception as e:
            self.get_logger().error(f'加载颜色配置失败: {e}')
            sys.exit(1)

    def get_parameters_from_server(self, param_names):
        """从参数服务器获取指定的参数列表"""
        client = self.create_client(GetParameters, '/puppy/get_parameters')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Waiting for parameter service...')

        request = GetParameters.Request()
        request.names = param_names
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            param_values = {
                name: value.double_value
                for name, value in zip(param_names, future.result().values)
                if value.type != ParameterType.PARAMETER_NOT_SET
            }
            return param_values
        else:
            self.get_logger().error('Failed to get parameters from server')
            return {}

    def check_parameter_values(self, param_values, param_names):
        """检查参数是否齐全"""
        missing_params = [param for param in param_names if param not in param_values]
        if missing_params:
            self.get_logger().error(f'Missing parameters: {missing_params}')
            return False
        return True

    def publish_initial_pose_and_gait(self):
        """发布初始化的机器人姿态和步态"""
        pose_msg = Pose(
            stance_x=self.PuppyPose['PuppyPose_LookDown_10deg_stance_x'],
            stance_y=self.PuppyPose['PuppyPose_LookDown_10deg_stance_y'],
            x_shift=self.PuppyPose['PuppyPose_LookDown_10deg_x_shift'],
            height=self.PuppyPose['PuppyPose_LookDown_10deg_height'],
            roll=self.PuppyPose['PuppyPose_LookDown_10deg_roll'],
            pitch=self.PuppyPose['PuppyPose_LookDown_10deg_pitch'],
            yaw=self.PuppyPose['PuppyPose_LookDown_10deg_yaw'],
            run_time=500
        )
        self.PuppyPosePub.publish(pose_msg)

        gait_msg = Gait(
            overlap_time=self.GaitConfig['GaitConfigFast_overlap_time'],
            swing_time=self.GaitConfig['GaitConfigFast_swing_time'],
            clearance_time=self.GaitConfig['GaitConfigFast_clearance_time'],
            z_clearance=self.GaitConfig['GaitConfigFast_z_clearance']
        )
        self.PuppyGaitConfigPub.publish(gait_msg)

    def move(self):
        """处理机器人移动逻辑"""
        global puppyStatus, puppyStatusLast
        up_stairs_time = 0
        time.sleep(2)

        while not self.is_shutdown:
            time.sleep(0.01)

            if puppyStatus == PuppyStatus.LOOKING_FOR:
                if target_centre_point is not None and target_centre_point[1] > 400:
                    puppyStatus = PuppyStatus.FOUND_TARGET
                    time.sleep(2.1)  # 继续往前走一点
                    self.PuppyVelocityPub.publish(Velocity(x=0.0, y=0.0, yaw_rate=0.0))
                    up_stairs_time = time.time()
                else:
                    self.PuppyVelocityPub.publish(Velocity(x=10.0, y=0.0, yaw_rate=0.0))

            elif puppyStatus == PuppyStatus.FOUND_TARGET:
                # 异步调用动作组
                asyncio.run(self.run_action_group('up_stairs_2cm.d6ac', True))
                if time.time() - up_stairs_time > 25:
                    puppyStatus = PuppyStatus.DOWN_STAIRS
                    self.PuppyPosePub.publish(Pose(
                        stance_x=self.PuppyPose['PuppyPose_LookDown_10deg_stance_x'],
                        stance_y=self.PuppyPose['PuppyPose_LookDown_10deg_stance_y'],
                        x_shift=self.PuppyPose['PuppyPose_LookDown_10deg_x_shift'],
                        height=self.PuppyPose['PuppyPose_LookDown_10deg_height'],
                        roll=self.PuppyPose['PuppyPose_LookDown_10deg_roll'],
                        pitch=self.PuppyPose['PuppyPose_LookDown_10deg_pitch'],
                        yaw=self.PuppyPose['PuppyPose_LookDown_10deg_yaw'],
                        run_time=500
                    ))
                    time.sleep(0.5)

            elif puppyStatus == PuppyStatus.DOWN_STAIRS:
                self.PuppyVelocityPub.publish(Velocity(x=14.0, y=0.0, yaw_rate=0.0))
                time.sleep(0.1)

            if puppyStatusLast != puppyStatus:
                self.get_logger().info(f'puppyStatus changed from {puppyStatusLast} to {puppyStatus}')
        puppyStatusLast = puppyStatus

    def image_callback(self, ros_image):
        """图像回调函数，处理图像并检测颜色目标"""
        try:
            # 使用CvBridge将ROS的Image消息转换为OpenCV的图像
            cv_image = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")
            # 图像处理
            frame_result = self.run(cv_image)
            cv2.imshow('Frame', frame_result)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f"Failed to process image: {e}")

    def run(self, img):
        """图像处理逻辑，检测目标颜色"""
        global target_centre_point
        
        # 转换为LAB色彩空间
        img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        detected_color = None

        for color_name, color_range in self.color_range_list.items():
            if color_name == 'red':  
                detected_color = color_name
                frame_mask = cv2.inRange(
                    img_lab, 
                    np.array(color_range['min'], dtype=np.uint8), 
                    np.array(color_range['max'], dtype=np.uint8)
                )
                break

        if detected_color:
            # 开运算和闭运算
            frame_open = cv2.morphologyEx(frame_mask, cv2.MORPH_OPEN, np.ones((6, 6), np.uint8))
            frame_closed = cv2.morphologyEx(frame_open, cv2.MORPH_CLOSE, np.ones((6, 6), np.uint8))

            # 找出最大轮廓
            contours, _ = cv2.findContours(frame_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                contour_max, area_max = self.get_area_max_contour(contours)
                if contour_max is not None and area_max > 100:
                    # 获取目标位置
                    rect = cv2.minAreaRect(contour_max)
                    box = np.int0(cv2.boxPoints(rect))
                    target_centre_point = [int(rect[0][0]), int(rect[0][1])]
                    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
                    cv2.circle(img, tuple(target_centre_point), 5, (0, 255, 0), -1)
        else:
            target_centre_point = None

        return img

    def get_area_max_contour(self, contours):
        """找出面积最大的轮廓"""
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour
        return max_contour, max_area

    async def run_action_group(self, action_name, wait):
        """调用动作组服务"""
        request = SetRunActionName.Request()
        request.name = action_name
        request.wait = wait

        future = self.runActionGroup_srv.call_async(request)

        try:
            result = await future  # 等待异步结果
            if result.success:
                self.get_logger().info(f"Action {action_name} executed successfully.")
            else:
                self.get_logger().error(f"Failed to execute action {action_name}.")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    puppy_node = PuppyStairClimbing()
    
    try:
        rclpy.spin(puppy_node)
    except KeyboardInterrupt:
        puppy_node.get_logger().info('Shutting down')
    finally:
        puppy_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

