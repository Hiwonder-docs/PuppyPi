# 7. ROS1-AI Vision and Tracking Course

<p id="anchor_1"></p>

## 7.1 Color Threshold Adjustment

Different light source will have different influence on the colors, which will results in recognition discrepancy. If this discrepancy hinder function from realizing, we need to tackle this problem with LAB_Tool. 

### 7.1.1 Open LAB_Tool

(1) Open VNC software, double click<img src="../_static/media/chapter_13/section_1/image2.png" style="width:0.31458in;height:0.31458in" />to open LAB_Tool.

(2) Then click "execute" in the pop-up window. 

(3) The interface of LAB_Tool is as follow.

<img src="../_static/media/chapter_13/section_1/image4.png"  alt="loading" />

:::{Note}
if there is not camera returned image, it means that the camera is not connected. Please check the camera wiring.
:::

### 7.1.2 LAB_Tool Layout

The interface is divided into two parts, including image display zone and recognition adjustment zone.

| Zone | Zone Layout |
|----|----|
| image display zone | <img src="../_static/media/chapter_13/section_1/image4.png" style=" " alt="loading" /> |
| recognition adjustment zone | <img src="../_static/media/chapter_13/section_1/image4.png" style=" " alt="loading" /> |

**(1)  Image Display Zone**

| Icon | Function |
|----|----|
| <img src="../_static/media/chapter_13/section_1/image4.png" style=" " alt="loading" /> | At left, it is the original image. At right, it is the processed image. |

**(2) Recognition Adjustment Zone**

| Icon | Function |
|----|----|
| <img src="../_static/media/chapter_13/section_1/image5.png" style="width:1.1811in;height:0.34125in" alt="loading" /> | Used to adjust L component of the image. Its function is the same as that of A and B sliders. |
| <img src="../_static/media/chapter_13/section_1/image4.png" style=" " alt="loading" /> | Select the recognized color to adjust |
| <img src="../_static/media/chapter_13/section_1/image6.png" style="width:0.7874in;height:0.32672in" alt="loading" /> | Save the adjusted value |
| <img src="../_static/media/chapter_13/section_1/image7.png" style="width:0.7874in;height:0.35295in" alt="loading" /> | Add new colors |

### 7.1.3 Adjust Default Color

Take adjusting red color for example. The following operation steps are also applicable to modifying other colors.

(1) Open LAB_Tool. When the camera is ready, select **"red"** in the drop-down menu.

<img class="common_img" src="../_static/media/chapter_13/section_1/image8.png"  alt="loading" />

(2) Modify all the values in **"min"** as 0, and **"max"** area as 255. 

<img class="common_img" src="../_static/media/chapter_13/section_1/image9.png"  />

(3) Face the camera to the red block. Drag L, A and B sliders to adjust the color threshold till the red block at left turns white and other area turns black. 

<img class="common_img" src="../_static/media/chapter_13/section_1/image10.png"  alt="loading" />

**LAB Threshold Adjustment Parameter**

| Color Component | Range | Corresponding Color Zone |
| --------------- | ----- | ------------------------ |
| L               | 0~255 | Black-White（-L ~ +L）   |
| A               | 0~255 | Green-Red（-a ~ +a）     |
| B               | 0~255 | Blue-Yellow（-b ~ +b）   |

**LAB Color Space**

<img class="common_img" src="../_static/media/chapter_13/section_1/image11.png"  style="width:300px;" />

We need to adjust the value of L, A and B to approach the zone of the recognized color. Take "red" for example, and please follow these steps to adjust.

(1) Firstly, set all the parameters at left as 0, and at right as 255.

(2) In **"LAB Color Space"**, all types of red are around **"+a"**, hence we need to increase A component. Remain the A max value at right unchanged. And increase the A min value at left till the red block at left turns white and other area turns black.

(3) Based on the environment, modify the value of **"L"** and **"B"**. If it belongs to light red, increase L min value at left. Otherwise, decrease L max value at right. If it belongs to warm tone, increase B min value at left. Otherwise, decrease B max at right.

(4) Click **"Save"** button to keep the adjusted value.

<img class="common_img" src="../_static/media/chapter_13/section_1/image12.png"  alt="loading" />

### 7.1.4 Add New Recognition Color

Besides three built-in recognized colors, we can add other recognized color in two ways.

(1) Directly modify the LAB value of red, blue or green as the actual LAB value of the new color.

(2) Use **"Add"** button to add new color option.

Method ① is more convenient. Take adding orange with method ① for example. The specific operation steps are as follow.

Take adding orange color as example. Follow the steps below to operate.

① Open LAB_Tool. After the camera is ready, select "red" in the drop-down menu.

 <img class="common_img" src="../_static/media/chapter_13/section_1/image8.png"  alt="loading" />

② Face the camera to the orange object. And then drag the slider of L, A and B to adjust the color threshold till the orange ball at left turns white and other area turns black

<img class="common_img" src="../_static/media/chapter_13/section_1/image13.png"  alt="loading" />

③ Click **"Save"** buttons to keep the modified data.

<img class="common_img" src="../_static/media/chapter_13/section_1/image14.png"  alt="loading" />


## 7.2 Color Recognition

### 7.2.1 Program Logic

Firstly, program to recognize color. Use Lab color space to convert the image from RGB into Lab.

Then, perform binaryzation, corrosion, dilation, etc., on the image to obtain the maximum contour which contains the target color.

Lastly, display the recognition result on the camera returned image and terminal interface.

### 7.2.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2) Click<img src="../_static/media/chapter_13/section_2/image3.png" style="width:0.32292in;height:0.30208in" /> or press **"Ctrl+Alt+T"** to open command line terminal.

(3) Input command **"rosrun puppy_standard_functions color_detect_demo.py"** and press Enter to start color recognition.

```bash
rosrun puppy_standard_functions color_detect_demo.py
```

(4) If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

### 7.2.3 Program Outcome

When red, green or blue is recognized, the color type will be displayed on camera returned image and the terminal.

For example, when red block is recognized, "red" will show up. 

<img class="common_img" src="../_static/media/chapter_13/section_2/image8.png"  />

<img src="../_static/media/chapter_13/section_2/image9.png"  />

### 7.2.4 Program Analysis

The source code of this program is located in: [/home/pi/puppy_pi/src/puppy_standard_functions/scripts/color_detect_demo.py](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/color_detect_demo.py)

- #### Image Processing

**(1) Gaussian filtering**

Before converting the image from RGB into Lab space, denoise the image and use GaussianBlur() function in cv2 library for Gaussian filtering.

```py
 frame_gb = cv2.GaussianBlur(frame_resize, (3, 3), 3) 
```

The meaning of the parameters in bracket is as follow

The first parameter `frame_resize` is the input image

The second parameter `(3, 3)` is the size of Gaussian kernel

The third parameter `3` is the allowable variance around the average in Gaussian filtering. The larger the value, the larger the allowable variance

**(2) Binaryzation Processing**

Adopt `inRange()` function in cv2 library to perform binaryzation on the image.

```py
frame_mask = cv2.inRange(frame_lab,
                                            (color_range_list[i]['min'][0],
                                            color_range_list[i]['min'][1],
                                            color_range_list[i]['min'][2]),
                                            (color_range_list[i]['max'][0],
                                            color_range_list[i]['max'][1],
                                            color_range_list[i]['max'][2]))  #对原图像和掩模进行位运算(perform bitwise operation to original image and mask)
```

The first parameter in the bracket is the input image. The second and the third parameters respectively are the lower limit and upper limit of the threshold. When the RGB value of the pixel is between the upper limit and lower limit, the pixel is assigned 1, otherwise, 0.
To reduce the interference and make the image smoother, it is necessary to perform corrosion and dilation on the image.

**(3) Corrosion and dilation treatment**

To reduce the interference and make the image smoother, it is necessary to perform corrosion and dilation on the image.

```py
eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  #腐蚀(corrosion)
dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))) #膨胀(dilation)
```

`erode()` function is used for corrosion. Take `eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))` for example. The meaning of the parameters in bracket are as follow.

① The first parameter `frame_mask` is the input image.

② The second parameter `cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))` is the structural element and kernel deciding the nature of the operation. And the first parameter in the parenthesis is the kernel shape and the second parameter is the kernel dimension.

`dilate()` function is used for image dilation. And the meaning of the parameters in parenthesis is the same as that of erode() function.

**(4) Acquire the maximum contour**

① After processing the image, acquire the contour of the target to be recognized, which involves `findContours()` function in cv2 library.

```py
contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  #找出轮廓(find out contour)
```

The first parameter in parentheses is the input image; the second parameter is the retrieval mode of the contour; the third parameter is the approximation method of the contour.

② Find the contour of the maximum area among the obtained contours. To avoid interference, please set a minimum value. Only when the area is larger than this value, the target contour is valid.

```py
if contour_area_temp > 50:  # 只有在面积大于50时，最大面积的轮廓才是有效的，以过滤干扰(only when the area is greater than 50, the contour with the maximal area is considered valid to filter the interference)
                area_max_contour = c
```

- #### Feedback information

(1)  After the contour of the maximum area is obtained, call circle() function in cv2 library, and circle the recognized target. The color of the circle is in line with the recognized color.

```py
cv2.circle(img, (centerX, centerY), radius, range_rgb[color_area_max], 2)#画圆(draw circle)
```

(2) Then call `print()` function to print the recognized color on the terminal.

```py
print('detect_color is',detect_color)  
```

(3)  Use `putText()` function in cv2 library to print the recognized color on the camera returned image.

```py
cv2.putText(img, "Color: " + detect_color, (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, draw_color, 2)
```

The first parameter  `img`  is the input image.

The second parameter  `"Color: " + detect_color`  represents the displayed content.

The third parameter  `(10, img.shape[0] - 10)` is where to display.

The fourth parameter `cv2.FONT_HERSHEY_SIMPLEX`  represents the font type.

The fifth parameter  `0.65`  represents the font size.

The sixth parameter  `draw_color` represents the color of the font.

The seventh parameter  `2`  represents the font weight.

### 2.5 Function Extension

**2.5.1 Add new recognized color**

In addition to the three built-in recognized colors, we can also set other colors for recognition. For example, let's take orange as an additional color for recognition. The specific modification steps are as follows:

(1) Based on "[7.1 Color Threshold Adjustment]()", use LAB_TOOL to add orange and save it. 

<img class="common_img" src="../_static/media/chapter_13/section_2/image10.png"  />

(2) After saving the orange, we can open the command window, input command "sudo vim puppy_pi/src/lab_config/config/lab_config.yaml" and press Enter.

```bash
sudo vim puppypi/src/lab_config/config/lab_config.yaml
```

Find the LAB value of the orange color we added in the opened file.

<img src="../_static/media/chapter_13/section_2/image13.png"  />

(3) Open the new command window and input the command "sudo vim puppy_pi/src/lab_config/lab_config_list.yaml".

```bash
sudo vim puppypi/src/lab_config/lab_config_list.yaml
```

Write the value of orange found in the previous file into the lab_config_list file and save it.

<img src="../_static/media/chapter_13/section_2/image16.png"  />

(4)  Input the command "sudo vim puppy_pi/src/puppy_standard_functions/scripts/color_detect_demo.py" in the command window to open program file.

```bash
sudo vim puppypi/src/puppy_standard_functions/scripts/color_detect_demo.py
```

In the program file, add the BGR value of the font color in the feedback screen.

<img src="../_static/media/chapter_13/section_2/image19.png"  />

:::{Note}
The three values here present the BGR values, solely serving as the color values for the front in the feedback screen, without affecting the recognition performance. You can modify the specific BGR values by looking up color-related BGR values on websites.

The values (0, 128, 255) here represent the BGR for orange.
:::

The following part of the program is the key code for color recognition. We need to add the LAB value for orange in it.

<img src="../_static/media/chapter_13/section_2/image21.png"  />

<img src="../_static/media/chapter_13/section_2/image23.png"  />

<img src="../_static/media/chapter_13/section_2/image25.png"  />

(5) After adding the code at the indicated location, enter the command to restart the game. Place an orange object in front of the camera, and you should see the orange color being recognized in the feedback screen. Additionally, in the command window, you should see the message "detect_color is orange" printed.

<img src="../_static/media/chapter_13/section_2/image27.png"  />

## 7.3 Tag Recognition

### 7.3.1 Program Logic

Firstly, program to recognize tag, which involves image graying, positioning and other operations. 
Lastly, encode and decode the tag, and display the recognition result on the camera returned image and terminal interface.

### 7.3.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::


(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_3/image4.png" style="width:0.32292in;height:0.30208in" /> or press "Ctrl+Alt+T" to open command line terminal.

(3)  If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

```bash
rosrun puppy_standard_functions apriltag_detect_demo.py
```

(4) If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

### 7.3.3 Program Outcome

After the game starts, place the tag card within the camera frame. When recognizing the tag, Tag ID will be printed on the camera returned image. And tag ID and coordinate will also be printed on the terminal.

<img class="common_img" src="../_static/media/chapter_13/section_3/image9.png"  />

<img src="../_static/media/chapter_13/section_3/image10.png"  />

### 7.3.4 Program Analysis 

The source code of this program is stored in :

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/apriltag_detect_demo.py](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/apriltag_detect_demo.py)

- #### Tag Detection

**(1) Image Graying**

Call `cvtColor()` function in cv2 library to convert the collected colored image into grayscale image and collect the tag information. 

```py
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
detections = detector.detect(gray, return_image=False)
```

**(2) Extract Tag Information**

After collecting the tag information, extract the useful information.

```py
        for detection in detections:
            M,e0,e1 = detector.detection_pose(detection,[camera_intrinsic.item(0,0), camera_intrinsic.item(1,1),
                                                                camera_intrinsic.item(0,2), camera_intrinsic.item(1,2)],
                                                                0.033)
                    
            P = M[:3,:4]
            coordinate=np.matmul(P,np.array([[0],[0],[0],[1]])).flatten()
            print('coordinate =',coordinate)  
```

```py
            tag_family = str(detection.tag_family, encoding='utf-8')  # 获取tag_family(get tag_family)
            times = 0
            if tag_family == 'tag36h11':
                tag_id = str(detection.tag_id)  # 获取tag_id(get tag_id)
                print('tag_id =',tag_id)
                return tag_id
            else:
                return None
```

`coordinate` represents the tag coordinate, `tag_family` refers to the type of tag, and `tag_id` indicates tag ID.

- #### **Feedback Information**

(1) After recognition, call `print()` function to print the tag coordinate and ID on the terminal.

```py
print('coordinate =',coordinate)   
```

```py  
print('tag_id =',tag_id)
```

(2) Then, call `putText()` function in cv2 library to print tag ID on the camera returned image.

```py
    cv2.putText(img, tag_id, (10, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
    return img
```

The meaning of the parameters in bracket is as follow.

The first parameter `img` is the input image.

The second parameter `tag_id` is the added text, referring to tag ID.

The third parameter `(10, img.shape[0] - 20)` is the coordinate of upper left corner of the added text.

The fourth parameter `cv2.FONT_HERSHEY_SIMPLEX` is the font type.

The fifth parameter  `2`  is the font size.

The sixth parameter `(0, 255, 255)` is the color of the font, and the values respectively corresponds to B, G, R. The color here is yellow.

The seventh parameter "3" is the font weight.

## 7.4 AR Vision

### 7.4.1 Program Logic 

Firstly, program to recognize tag, which involves image graying, positioning and other operations.

Next, encode and decode the tag to acquire information of the tag. 

Lastly, through model projection, polygon fill and other operations, draw 3D image on the designated area of camera returned image, and print Tag information on the camera returned image and terminal interface. 

### 7.4.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_4/image4.png" style="width:0.32292in;height:0.30208in" />or press "Ctrl+Alt+T" to open command line terminal

(3)  Input the command and press Enter to start AR vision.

```bash
rosrun puppy_standard_functions apriltag_AR_demo.py
```

(4) If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

### 7.4.3 Program Outcome

After the game starts, place the tag card within the camera frame. When the tag is recognized, four corners of the tag will be marked by blue dots, and the 3D image will be displayed on the tag. Besides, the tag ID and coordinate will be printed on the terminal. 

<img class="common_img" src="../_static/media/chapter_13/section_4/image8.png"  />

<img src="../_static/media/chapter_13/section_4/image9.png"  />

### 7.4.4 Program Analysis

The source code of this program is stored in /home/pi/puppy_pi/src/puppy_standard_functions/scripts/apriltag_AR_demo.py 

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/apriltag_AR_demo.py ](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/apriltag_AR_demo.py)

- #### Tag Detection

**(1) Image Graying**

Call `cvtColor()` function in cv2 library to convert the collected colored image into grayscale image and collect the tag information.

```py
gray = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
detections = self.tag_detector.detect(gray)
```

**(2) Extract Tag Information**

After collecting the tag information, extract the useful information.

```py
for detection in detections:
 M,e0,e1 = self.tag_detector.detection_pose(detection,[self.camera_intrinsic.item(0,0), self.camera_intrinsic.item(1,1),
            self.camera_intrinsic.item(0,2), self.camera_intrinsic.item(1,2)],0.033)
                    
 P = M[:3,:4]
coordinate=np.matmul(P,np.array([[0],[0],[0],[1]]))
```

```py
tag_id = detection.tag_id
tag_center = detection.center
tag_corners = detection.corners
```

`coordinate`  represents the tag coordinate, `tag_family` refers to the type of tag, and  `tag_id`  indicates tag ID.

- #### 3D Image Drawing 

**(1) Relative Pose Calculation**

Firstly, acquire the pose of the camera relative to the world coordinate system, that is the rotation vector and translation vector from the world coordinate system to the camera coordinate system. solvePnP() function in cv2 library will be called.

```py
ret, rvecs, tvecs = cv2.solvePnP(OBJP, corners, self.camera_intrinsic, self.dist_coeffs)
```

The meaning of the parameters in bracket is as follow. 

The first parameter `OBJP` is the intrinsic matrix of the camera.

The second parameter `corners` is the distortion parameter of the camera.

The third parameter `self.camera_intrinsic` is the 3D coordinate in mm under world coordinate system.

The fourth parameter `self.dist_coeffs` is the 2D coordinate in pixel under camera coordinate system

**(2) Model Projection**

After the pose of the camera relative to the world coordinate system is required, call `projectPoints()` function in cv2 library to convert the 3D coordinate under world coordinate system into 2D coordinate under pixel coordinate system  

```py
imgpts, jac = cv2.projectPoints(AXIS, rvecs, tvecs, self.camera_intrinsic, self.dist_coeffs)
```

**(3) Image Drawing**

The program is default to draw 3D bicycle

```py
ar_app_node.set_model_srv_callback('bicycle')
```

And other 3D models are available, including cow, fox, rat, wolf, pirate-ship-fat and rectangle.

```py
MODEL_PATH = '/home/ubuntu/puppypi/src/puppy_standard_functions/models'
```

① Color the rectangle through calling `drawContours()` and `line()` function in cv2 library.

```py
if self.target_model == 'rectangle':
    imgpts, jac = cv2.projectPoints(AXIS, rvecs, tvecs, self.camera_intrinsic, self.dist_coeffs)
     result_image = draw(result_image, corners, imgpts)
```

```py
def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    cv2.drawContours(img, [imgpts[:4]],-1,(0, 255, 0),-3)
    for i,j in zip(range(4),range(4,8)):
        cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    cv2.drawContours(img, [imgpts[4:]],-1,(0, 0, 255),3)
    return img
```

② Call `fillConvexPoly()` function to color other patterns.

```py
else:
     for points, color in self.obj:
          dst, jac = cv2.projectPoints(points.reshape(-1, 1, 3)/100.0, rvecs, tvecs, self.camera_intrinsic, self.dist_coeffs)
          imgpts = dst.astype(int)
                             # 手动上色(manually apply color)
           if self.target_model == 'cow':
               cv2.fillConvexPoly(result_image, imgpts, (0, 255, 255))
           elif self.target_model == 'wolf':
                cv2.fillConvexPoly(result_image, imgpts, (255, 255, 0))
            else:
                cv2.fillConvexPoly(result_image, imgpts, color)
```

Take `cv2.fillConvexPoly(result_image, imgpts, (255, 255, 0)` for example. The meaning of the parameters in bracket is as follow.

The first parameter `result_image` is the input image.

The second parameter `imgpts` is the vertex of the polygon.

The third parameter `(255, 255, 0)` is the filled color. The values respectively corresponds to R, G and B, and refers to yellow.

- #### Feedback Information

**(1) Image Output**

Call `imshow()` function in cv2 library to display the image on camera returned image.

```py
cv2.imshow('image', cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR))
```

The meaning of the parameters in bracket is as follow.

The first parameter `image` is the window name and the data type is string.

The second parameter `frame_result` is the input image.

**(2) Print Tag Information**

Call print() function to print tag coordinate and ID on the terminal.

```py
print('coordinate = ',coordinate)
```

```py
print('tag_id = ',tag_id)
```

### 7.4.5 Function Extension

- #### Change Default Displayed Image

The program is default to display 3D bicycle. And other 3D models are available, including cow, fox, rat, wolf, pirate-ship-fat and rectangle. 
For example, we can modify the program to display 3D cow. We need to take 6 steps to realize this. 

(1)  Click<img src="../_static/media/chapter_13/section_4/image6.png" style="width:0.31458in;height:0.27361in" /> at upper left corner or press **"Ctrl+Alt+T"** to open command line terminal.

(2) Input command  `rosed puppy_standard_functions apriltag_AR_demo.py` and press Enter to open the program file.

```bash
rosed puppy_standard_functions apriltag_AR_demo.py
```

(3) Please jump to this line of code.

<img src="../_static/media/chapter_13/section_4/image12.png" class="common_img"  />

:::{Note}
input the line number and press **"Shift+G"** to jump to the corresponding line.
:::

(4) Press **"i"** key to enter editing mode and modify the code as **"ar_app_node.set_model_srv_callback('cow')".**

<img src="../_static/media/chapter_13/section_4/image14.png"  />

(5) After modification, press **"Esc"**, input **":wq"** and press Enter to save and exit the editing.

```bash
:wq
```

(6) Input the command to restart the game, and then the 3D cow image will be displayed on the camera returned image.

```bash
rosrun puppy_standard_functions apriltag_AR_demo.py
```

## 7.5 Colored Block Positioning

### 7.5.1 Program Logic

Firstly, program to recognize color. Use Lab color space to convert the image from RGB into Lab.

Then, perform binaryzation, corrosion, dilation, etc., on the image to obtain the maximum contour which contains the target color.

Lastly, display the recognition result on the camera returned image and terminal interface.

### 7.5.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_5/image4.png" style="width:0.32292in;height:0.30208in" />or press "**Ctrl+Alt+T**" to open command line terminal.

(3) Input command "rosrun puppy_standard_functions color_tracking_demo.py" and press Enter to start the game.

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

(4) If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

### 7.5.3 Program Outcome

After the game starts, place the red block within the camera frame. When the colored block is recognized, the block will be marked with red circle and its coordinate will be printed on the terminal.

<img class="common_img" src="../_static/media/chapter_13/section_5/image9.png"  />

<img src="../_static/media/chapter_13/section_5/image10.png"  />

### 7.5.4 Program Analysis

The source code of this program lies in 

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/color_tracking_demo.py](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/color_tracking_demo.py)

- #### Image Processing

**(1) Binaryzation Processing**

Adopt `inRange()` function in cv2 library to perform binaryzation on the image.

```py
frame_mask = cv2.inRange(frame_lab, tuple(target_color_range['min']), tuple(target_color_range['max']))  # 对原图像和掩模进行位运算(perform bitwise operation to original image and mask)
```

The first parameter in the bracket is the input image. The second and the third parameters respectively are the lower limit and upper limit of the threshold. When the RGB value of the pixel is between the upper limit and lower limit, the pixel is assigned 1, otherwise, 0.

**(2) Corrosion and Dilation**

To reduce the interference and make the image smoother, it is necessary to perform corrosion and dilation on the image.

```py
eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 腐蚀(corrosion)
dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 膨胀(dilation)
```

`erode()` function is used for corrosion. Take `eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))` for example. The meaning of the parameters in bracket are as follow.

The first parameter `frame_mask` is the input image.

The second parameter `cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))` is the structural element and kernel deciding the nature of the operation. And the first parameter in the parenthesis is the kernel shape and the second parameter is the kernel dimension.

`dilate()` function is used for image dilation. And the meaning of the parameters in parenthesis is the same as that of `erode()` function.

**(3)  Acquire the Maximum Contour**

After processing the image, acquire the contour of the target to be recognized, which involves findContours() function in cv2 library.

```py
contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # 找出轮廓(find out the contour)
```

The first parameter in parentheses is the input image; the second parameter is the retrieval mode of the contour; the third parameter is the approximation method of the contour.

(2) Find the contour of the maximum area among the obtained contours. To avoid interference, please set a minimum value. Only when the area is larger than this value, the target contour is valid.

```py
  if contour_area_temp > 10:  # 只有在面积大于300时，最大面积的轮廓才是有效的，以过滤干扰(only when the area is greater than 300, the contour with the maximal area is valid to filter the interference)
       area_max_contour = c
```

- #### Feedback Information 

**(1) Coordinate Feedback**

Call print() function to print the coordinate of the colored block on the camera returned image. 

```py
 print('center_x = %d ,center_y=%d'%(int(center_x), int(center_y)))
```

**(2) Block Marking**

Use circle() function in cv2 library to circle the colored block in corresponding color

```py
cv2.circle(img, (int(center_x), int(center_y)), int(radius), range_rgb[__target_color], 2)
```

The meaning of the parameters in the bracket is as follow.

The first parameter `img` is the input image

The second parameter `(int(center_x), int(center_y))` is the center coordinate

The third parameter `int(radius)` is the radius of the circle

The fourth parameter `range_rgb[__target_color]` is the color of the circle

The fifth parameter `2` is thickness of the circle.

### 7.5.5 Function Extension

<p id="anchor_5_4_1"></p>

- #### Modify Default Recognition Color

There are three built-in colors, including red, green and blue. The default recognized color is red.

Take modifying the default recognition color as green for example. The specific operation steps are as follow.

(1)  Click <img src="../_static/media/chapter_13/section_5/image6.png" style="width:0.31458in;height:0.27361in" />or press "**Ctrl+Alt+T**" to open command line terminal

(2) Input the command and press Enter to open program file.

```bash
rosed puppy_standard_functions color_tracking_demo.py
```

(3) Then, jump to this line of code.

<img src="../_static/media/chapter_13/section_5/image13.png"  />

:::{Note}
 we can input the line number and press **"Shift+G"** to jump to the corresponding line.
:::

(4) Press **"i"** to enter the editing mode. Modify the code as `msg.data = 'green'`.

<img class="common_img" src="../_static/media/chapter_13/section_5/image14.png"  />

(5) After modification, Press **"Esc"** and input **":wq"** and then press Enter to save the file and exit the editor.

```bash
:wq
```

(6 Input command `rosrun puppy_standard_functions color_tracking_demo.py` to restart the game. Then PuppyPi will recognize green.

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

- #### Add New Recognition Color

In addition to the built-in recognized colors, you can add other recognition colors in the program. Take adding yellow as example.

(1) Click <img src="../_static/media/chapter_13/section_5/image6.png" style="width:0.31458in;height:0.27361in" />or press "**Ctrl+Alt+T**" to open command line terminal

(2) Input command **"rosed lab_config lab_config.yaml"** and press Enter to open Lab color setting document. It is recommended to screenshot the initial value for recording.

```bash
rosed lab_config lab_config.yaml
```

<img class="common_img" src="../_static/media/chapter_13/section_5/image21.png"  />

(3)  Double click the <img src="../_static/media/chapter_13/section_5/image23.png" style="width:0.31496in;height:0.29528in" /> in the system desktop to open color threshold adjustment tool. If the prompt box pops up, just click **"Execute"**.

<img src="../_static/media/chapter_13/section_5/image24.png"  />

(4) Having entered the interface successfully, select **"red"** in the drop-down menu.

<img src="../_static/media/chapter_13/section_5/image25.png"  />

(5) Place the yellow object within the camera frame. Then Drag the sliders of L, A, and B until the yellow block at the left screen becomes white and other areas become black. 

<img src="../_static/media/chapter_13/section_5/image26.png"  />

(6) After adjustment, click **"Save"** to keep the data. Then we can close the tool.

<img src="../_static/media/chapter_13/section_5/image27.png"  />

(7) Check whether the modified data was successfully written in. Input the command **"rosed lab_config lab_config.yaml"** and press Enter to open Lab color setting file.  

```bash
rosed lab_config lab_config.yaml
```

<img class="common_img" src="../_static/media/chapter_13/section_5/image28.png"  />

:::{Note}
 In order to avoid the game performance, it's recommended to use the LAB_Tool to modify the value back to the initial value after the modification.
:::

(8)  According to the steps in "[7.5.5 Function Extension -> Modify Default Recognition Color]()", restore the default recognition color to red.

(9) Input the command and press Enter to restart Colored Block Positioning game. Place the yellow block within the camera frame. Then it will be circled on the camera returned image

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

## 7.6 Color Tracking

### 7.6.1 Program Logic

Firstly, program to recognize color. Use Lab color space to convert the image from RGB into Lab.

Then, perform binaryzation, corrosion, dilation, etc., on the image to obtain the maximum contour which contains the target color.

Next, acquire X-axis and Y-axis coordinates of the center of target contour. And adjust PuppyPi's pitch angle and roll angle according to the coordinate.

Lastly, obtain the rotation angle of the servo through inverse kinematics calculation, and program the servo to rotate to the designated angle. 

### 7.6.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_6/image4.png" style="width:0.32292in;height:0.30208in" /> or press "Ctrl+Alt+T" to open command line terminal

(3) Input command "rosrun puppy_standard_functions color_tracking_demo.py" and press Enter to start the game.

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

(4) If want to close this game, we can press "Ctrl+C". If it fails to close the game, please try again.

### 7.6.3 Program Outcome

After the game starts, place the red block within the camera frame. When recognizing the object, PuppyPi will adjust its posture according to the position of the object. Besides, the block will be marked with red circle on the camera returned image and its coordinate will be printed on the terminal.

<img src="../_static/media/chapter_13/section_6/image9.png"  />

### 7.6.4 Program Analysis

The source code of this program lies in 

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/color_tracking_demo.py](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/color_tracking_demo.py)

- #### Image Processing

**(1) Binaryzation Processing**

Adopt inRange() function in cv2 library to perform binaryzation on the image.

```py
frame_mask = cv2.inRange(frame_lab, tuple(target_color_range['min']), tuple(target_color_range['max']))  # 对原图像和掩模进行位运算(perform bitwise operation to original image and mask)
```

The first parameter in the bracket is the input image. The second and the third parameters respectively are the lower limit and upper limit of the threshold. When the RGB value of the pixel is between the upper limit and lower limit, the pixel is assigned 1, otherwise, 0.

**(2) Corrosion and Dilation**

To reduce the interference and make the image smoother, it is necessary to perform corrosion and dilation on the image.

```py
eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 腐蚀(corrosion)
dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 膨胀(dilation)
```

erode() function is used for corrosion. Take "eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))" for example. The meaning of the parameters in bracket are as follow.
The first parameter "frame_mask" is the input image.
The second parameter "cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))" is the structural element and kernel deciding the nature of the operation. And the first parameter in the parenthesis is the kernel shape and the second parameter is the kernel dimension.
dilate() function is used for image dilation. And the meaning of the parameters in parenthesis is the same as that of erode() function

**(3) Acquire the Maximum Contour**

After processing the image, acquire the contour of the target to be recognized, which involves findContours() function in cv2 library.

```py
contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # 找出轮廓(find out the contour)
```

The first parameter in parentheses is the input image; the second parameter is the retrieval mode of the contour; the third parameter is the approximation method of the contour.

```py
if contour_area_temp > 10:  # 只有在面积大于300时，最大面积的轮廓才是有效的，以过滤干扰(only when the area is greater than 300, the contour with the maximal area is valid to filter the interference)
    area_max_contour = c
```

- #### Feedback Information

**(1) Coordinate Feedback**

Call print() function to print the coordinate of the colored block on the camera returned image.

```py
print('center_x = %d ,center_y=%d'%(int(center_x), int(center_y)))
```

**(2) Block Marking**

Use circle() function in cv2 library to circle the colored block in corresponding color

```py
 cv2.circle(img, (int(center_x), int(center_y)), int(radius), range_rgb[__target_color], 2)
```

The meaning of the parameters in the bracket is as follow.

The first parameter `img` is the input image

The second parameter `(int(center_x), int(center_y))` is the center coordinate

The third parameter `int(radius)` is the radius of the circle

The fourth parameter `range_rgb[__target_color]` is the color of the circle

The fifth parameter `2` is thickness of the circle.

- #### Action Feedback

**(1)  Set Specific Point** 

Set the center of the camera returned image as the specific point. Then based on the position relation between the center of the target object and the specific point, determine PuppyPi to execute which action. 

```py
x_pid.SetPoint = img_w / 2.0  # 设定(set)
```

```py
z_pid.SetPoint = img_h / 2.0
```

**(2) Adjust Roll Angle**

Adjust PuppyPi's Roll angle according to whether the target center is at left or right of the camera returned image center.

```py
if abs(x_pid.SetPoint - center_x) > 230:
      x_pid.Kp = 0.004

   x_pid.update(center_x)

   x_dis = x_pid.output

   x_dis = np.radians(30) if x_dis > np.radians(30) else x_dis
   x_dis = np.radians(-30) if x_dis < np.radians(-30) else x_dis
   PuppyPose['roll'] = x_dis
```

**(3) Adjust Pitch Angle**

Adjust PuppyPi's Pitch angle according to whether the target center is below or above the camera returned image center.

```py
if abs(z_pid.SetPoint - center_y) > 180:
     z_pid.Kp = 0.002
z_pid.update(center_y)
z_dis = z_pid.output

z_dis = np.radians(30) if z_dis > np.radians(30) else z_dis
z_dis = np.radians(-20) if z_dis < np.radians(-20) else z_dis

PuppyPose['pitch'] = z_dis
```

### 7.6.5 Function Extension

- #### Modify Default Recognition Color

There are three built-in colors, including red, green and blue. The default recognized color is red.

Take modifying the default recognition color as green for example. The specific operation steps are as follow.

(1)  Click <img src="../_static/media/chapter_13/section_6/image6.png" style="width:0.31458in;height:0.27361in" />or press "**Ctrl+Alt+T**" to open command line terminal

(2)  Input command "rosed puppy_standard_functions color_tracking_demo.py" and press Enter to open program file.

```bash
rosed puppy_standard_functions color_tracking_demo.py
```

(3) Then, jump to this line of code.

<img src="../_static/media/chapter_13/section_6/image12.png"  />

:::{Note}
we can input the line number and press **"Shift+G"** to jump to the corresponding line.
:::

(4) Press "i" to enter the editing mode. Modify the code as `msg.data = 'green'`.

<img class="common_img" src="../_static/media/chapter_13/section_6/image13.png"  />

(5) After modification, Press **"Esc"** and input **":wq"** and then press Enter to save the file and exit the editor.

```bash
:wq
```

(6) Input command **"rosrun puppy_standard_functions color_tracking_demo.py"** to restart the game. Then PuppyPi will recognize green.

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

- #### Add New Recognition Color

In addition to the built-in recognized colors, you can add other recognition colors in the program. Take adding yellow as example.

(1)  Double click the<img src="../_static/media/chapter_13/section_6/image18.png" style="width:0.31496in;height:0.29548in" />in the system desktop to open color threshold adjustment tool. If the prompt box pops up, just click **"Execute"**.

<img src="../_static/media/chapter_13/section_6/image19.png"  />

(2)  Next, click **"Add"** button.

<img src="../_static/media/chapter_13/section_6/image20.png"  />

(3) Then enter **"yellow"** in the pop-up interface.

<img class="common_img" src="../_static/media/chapter_13/section_6/image21.png"  />

(4) Select **"yellow"** in the drop-down menu.

<img src="../_static/media/chapter_13/section_6/image22.png"  />

(5) Place the yellow object within the camera frame. Then Drag the sliders of L, A, and B until the yellow block at the left screen becomes white and other areas become black.

<img src="../_static/media/chapter_13/section_6/image23.png"  />

(6) After adjustment, click "Save" to keep the data. Then we can close the tool.

<img src="../_static/media/chapter_13/section_6/image24.png"  />

(7) Click <img src="../_static/media/chapter_13/section_6/image6.png" style="width:0.31458in;height:0.27361in" /> or press **"Ctrl+Alt+T"** to open command line terminal

(8) Check whether the modified data was successfully written in. Input the command **"rosed lab_config lab_config.yaml"** and press Enter to open Lab color setting file.

```bash
rosed lab_config lab_config.yaml
```

<img src="../_static/media/chapter_13/section_6/image26.png"  />

(9) According to the steps in "[7.6.5 Function Extension -> Modify Default Recognition Color]()", modify the default recognition color as yellow.

(10) Input command **"rosrun puppy_standard_functions color_tracking_demo.py"** and press Enter to restart the game. The PuppyPi will recognize yellow.

```bash
rosrun puppy_standard_functions color_tracking_demo.py
```

## 7.7 Tag Positioning

### 7.7.1 Program Logic

Firstly, program to recognize tag, which involves image graying, positioning and other operations.

Lastly, encode and decode the tag, and display the recognition result on the camera returned image and terminal interface.

### 7.7.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_7/image4.png" style="width:0.32292in;height:0.30208in" />or press "**Ctrl+Alt+T**" to open command line terminal

(3)  Input the command  and press Enter to start the game.

```bash
rosrun puppy_standard_functions apriltag_tracking_demo.py
```

(4) If want to close this game, we can press **"Ctrl+C"**. If it fails to close the game, please try again.

### 7.7.3 Program Outcome

After the game starts, place the tag card within the camera frame. When recognizing the tag, Tag ID will be printed on the camera returned image.

### 7.7.4 Program Analysis

The source code of this program is stored in 

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/apriltag_tracking_demo.py](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/apriltag_tracking_demo.py)

- #### Tag Detection

**(1) Image Graying**

Call `cvtColor()` function in cv2 library to convert the collected colored image into grayscale image and collect the tag information.

```py
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
detections = detector.detect(gray, return_image=False)
```

**(2) Extract Tag Information**

After collecting the tag information, extract the useful information.

```py
if len(detections) != 0:
    for detection in detections:
         M,e0,e1 = detector.detection_pose(detection,[camera_intrinsic.item(0,0), camera_intrinsic.item(1,1),
                                                                camera_intrinsic.item(0,2), camera_intrinsic.item(1,2)],
                                                                0.033)
                    
         P = M[:3,:4]
         coordinate=np.matmul(P,np.array([[0],[0],[0],[1]])).flatten()
```

```py
tag_family = str(detection.tag_family, encoding='utf-8')  # 获取tag_family(get tag_family)
```

```py
if tag_family == 'tag36h11':
   tag_id = str(detection.tag_id)  # 获取tag_id(get tag_id)
   return tag_id
```



`coordinate` represents the tag coordinate, `tag_family` refers to the type of tag, and `tag_id` indicates tag ID.

- #### Feedback Information

Call `putText()` function in cv2 library to print the tag ID on the camera returned image.

```py
cv2.putText(img, tag_id, (10, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
```

The meaning of the parameters in bracket is as follow.

The first parameter `img` is the input image.

The second parameter `tag_id` is the added text, referring to tag ID.

The third parameter `(10, img.shape[0] - 20)` is the coordinate of upper left corner of the added text.

The fourth parameter `cv2.FONT_HERSHEY_SIMPLEX` is the font type.

The fifth parameter `2` is the font size.

The sixth parameter `(0, 255, 255)` is the color of the font, and the values respectively corresponds to B, G, R. The color here is yellow.

The seventh parameter `3` is the font weight.



## 7.8 Tag Tracking

### 7.8.1 Program Logic

AprilTag is a visual positioning marker, which is similar to QR code or bar code. It can facilitate the tag detection and relative position calculation. It's mainly applied to AR, robot and camera calibration, etc.

The process of tag tracking is as follow.

Firstly, program to recognize tag, which involves image graying, positioning and other operations.

Next, encode and decode the tag, and display the recognition result on the camera returned image and terminal interface.

Then, according to the distance between the tag and the camera, control PuppyPi to move with the tag so as to realize tag tracking.

### 7.8.2 Operation Steps

:::{Note}
The input command should be case sensitive. And the key words can be complemented by "Tab" key.
:::

(1) Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_8/image4.png" style="width:0.32292in;height:0.30208in" />or press "**Ctrl+Alt+T**" to open command line terminal.

(3) Input the command and press Enter to start the game.

```bash
rosrun puppy_standard_functions apriltag_tracking_demo.py
```

(4) If want to close this game, we can press **"Ctrl+C"**. If it fails to close the game, please try again.

### 7.8.3 Program Outcome

After the game starts, place the tag card within the camera frame. When recognizing the tag, Tag ID will be printed on the camera returned image. If we move the tag, PuppyPi will move forward or backward.


### 7.8.4 Program Analysis

The source code of this program is stored in 

[/home/pi/puppy_pi/src/puppy_standard_functions/scripts/apriltag_tracking_demo.py ](https://store.hiwonder.com.cn/docs/PuppyPi/pi5/source_code/13/apriltag_tracking_demo.py)

- #### Tag Detection

**(1)  Image Graying**

Call `cvtColor()` function in cv2 library to convert the collected colored image into grayscale image and collect the tag information.

```py
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
detections = detector.detect(gray, return_image=False)
```

**(2)  Extract Tag Information**

After collecting the tag information, extract the useful information.

```py
if len(detections) != 0:
    for detection in detections:
        M,e0,e1 = detector.detection_pose(detection,[camera_intrinsic.item(0,0), camera_intrinsic.item(1,1),
                                                                camera_intrinsic.item(0,2), camera_intrinsic.item(1,2)],
                                                                0.033)
                    
         P = M[:3,:4]
         coordinate=np.matmul(P,np.array([[0],[0],[0],[1]])).flatten()
```

```py
tag_family = str(detection.tag_family, encoding='utf-8')  # 获取tag_family(get tag_family)
```

```py
if tag_family == 'tag36h11':
    tag_id = str(detection.tag_id)  # 获取tag_id(get tag_id)
    return tag_id 
```

`coordinate` represents the tag coordinate, `tag_family` refers to the type of tag, and `tag_id` indicates tag ID.

- #### Feedback Information

Call `putText()` function in cv2 library to print the tag ID on the camera returned image.

```py
cv2.putText(img, tag_id, (10, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
```

The meaning of the parameters in bracket is as follow.

The first parameter `img` is the input image.

The second parameter `tag_id` is the added text, referring to tag ID.

The third parameter `(10, img.shape[0] - 20)` is the coordinate of upper left corner of the added text.

The fourth parameter `cv2.FONT_HERSHEY_SIMPLEX` is the font type.

The fifth parameter `2` is the font size.

The sixth parameter `(0, 255, 255)` is the color of the font, and the values respectively corresponds to B, G, R. The color here is yellow.

The seventh parameter `3` is the font weight.

- #### Action Feedback

The program controls PuppyPi's movement through publishing topic.

```py
if coordinate is None:
   PuppyVelocityPub.publish(x=0, y=0, yaw_rate=0)
   rospy.sleep(0.01)   
else:
    if coordinate[2] > 0.22:
        PuppyVelocityPub.publish(x=5, y=0, yaw_rate=0)
    elif coordinate[2] < 0.18:
        PuppyVelocityPub.publish(x=-5, y=0, yaw_rate=0)
    else:
        PuppyVelocityPub.publish(x=0, y=0, yaw_rate=0)
```

The meaning of the parameters of `PuppyVelocityPub.publish()` is as follow. 

The first parameter is used to control PuppyPi to move straight. Moving forward is taken as the positive direction and Its unit is cm/s. When it is "0", PuppyPi will stay still. When it is positive, PuppyPi will move forward. When it is negative, PuppyPi will move backward. The greater the absolute value of the parameter, the larger the stride PuppyPi takes.   

The second parameter is used to control PuppyPi to walk sideways. Its unit is cm/s. As PuppyPi cannot walk sideways, this parameter is without actual function.

The third parameter is used to control PuppyPi to turn. The counterclockwise direction is taken as the positive direction, and the unit is rad/s. When the value is "0", PuppyPi will move straight. When the value is positive, PuppyPi will keep turning left as moving. When the value is negative, PuppyPi will keep turning right as moving. The greater the absolute value of the parameter, the greater PuppyPi turns. 

(1) When not recognizing the tag, PuppyPi will not take action.

```py
if coordinate is None:
   PuppyVelocityPub.publish(x=0, y=0, yaw_rate=0)
   rospy.sleep(0.01) 
```

(2)  When the distance between the tag and camera is greater than the set threshold, PuppyPi will move forward in 5cm/s.

```py
if coordinate[2] > 0.22:
    PuppyVelocityPub.publish(x=5, y=0, yaw_rate=0)
```

(3) When the distance between the tag and camera is smaller than the set threshold, PuppyPi will move backward in 5cm/s.

```py
elif coordinate[2] < 0.18:
   PuppyVelocityPub.publish(x=-5, y=0, yaw_rate=0)
```

### 7.8.5 Function Extension

- #### 8.5.1 Modify Default

The distance threshold has been set in the program, which is used to decide PuppyPi perform which action for feedback.

When the distance between the camera and tag is greater than 0.22m, PuppyPi will moves forward. When it is smaller than 0.18m, PuppyPi will move backward continuously till the distance is greater than or equal to 0.18m.

The distance threshold can be modified. For example, we program PuppyPi to move forward when the distance between the camera and tag is greater than 0.20m.

(1)  Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click<img src="../_static/media/chapter_13/section_8/image4.png" style="width:0.32292in;height:0.30208in" />or press "**Ctrl+Alt+T**" to open command line terminal.

(3) Input command **"rosed puppy_standard_functions apriltag_tracking_demo.py"** and press Enter to open the program file.

```bash
rosed puppy_standard_functions apriltag_tracking_demo.py
```

(4) Then jump to this line of code.

<img src="../_static/media/chapter_13/section_8/image12.png"  />

:::{Note}
 we can input the line number and press **"Shift+G"** to jump to the corresponding line.
:::

(5) Press **"i"** key to enter the editing mode, and then modify the code as `coordinate[2] > 0.20`.

<img src="../_static/media/chapter_13/section_8/image14.png"  />

(6) After modification, press **"Esc"** and input **":wq"** and press Enter to save and exit the editing.

```bash
:wq
```

(7) Input the command and press Enter to restart the game to check the PuppyPi's performance.

```bash
rosrun puppy_standard_functions apriltag_tracking_demo.py
```

- #### Change the Default Moving Speed

Both the default speed of moving forward and backward in the program have been set as 5cm/s. And we can modify the value. For example, modify the speed of moving forward as 3cm/s. 

(1)  Turn on PuppyPi, and then connect to Raspberry Pi desktop through VNC.

(2)  Click <img src="../_static/media/chapter_13/section_8/image4.png" style="width:0.32292in;height:0.30208in" /> or press "**Ctrl+Alt+T**" to open command line terminal

(3) Input the command and press Enter to open the program file.

```bash
rosed puppy_standard_functions apriltag_tracking_demo.py
```

(4) Then jump to this line of code.

<img src="../_static/media/chapter_13/section_8/image19.png"  />

:::{Note}
we can input the line number and press **"Shift+G"** to jump to the corresponding line.
:::

(5) Press "i" key to enter the editing mode, and then modify the code as `PuppyVelocityPub.publish(x=3, y=0, yaw_rate=0)`.

<img src="../_static/media/chapter_13/section_8/image21.png"  />

(6) After modification, press **"Esc"** and input **":wq"** and press Enter to save and exit the editing.

```bash
:wq
```

(7) Input the command and press Enter to restart the game to check the PuppyPi's performance.

```bash
rosrun puppy_standard_functions apriltag_tracking_demo.py
```
