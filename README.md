### README

#### **Motion Detection with Timestamps**

This Python code performs motion detection on a video and determines the start and end timestamps of the detected motion. It uses the OpenCV library to track motion through background subtraction and contour detection. When motion is detected, the start and end times are printed to the console.

---

#### **Required Libraries**

- **cv2 (OpenCV)**: Used for image processing and video handling.
- **numpy**: Used for numerical operations and matrix calculations.

---

#### **Installation**

To install the required libraries, run the following command:

```bash
pip install opencv-python numpy
```

---

#### **Code Explanation**

1. **Video Reading:**
   - The `cv.VideoCapture('video')` function opens the video file.
   - Replace `'video'` with the path to your video file.

2. **Background Subtractor:**
   - The `cv.createBackgroundSubtractorMOG2` function is used to create the background subtractor, which detects the differences between the current frame and the background.
   - `history=150`: Specifies the number of previous frames to retain in the background model.
   - `varThreshold=16`: Threshold value for detecting differences.
   - `detectShadows=True`: Detects shadows as well.

3. **Motion Detection:**
   - The `cv.findContours` function detects the external contours of any movement in the frame.
   - `cv.contourArea(contour) > 500`: If the area of the contour is greater than 500, it is considered motion. This value can be adjusted to filter out small noise.

4. **Timestamps:**
   - When motion is first detected, the start time is recorded.
   - When motion stops, the end time is recorded, and both start and end times are printed to the console.

5. **Displaying the Video:**
   - The `cv.imshow` function displays each frame of the video.
   - You can exit the video playback by pressing the 'q' key.

---

#### **Steps to Run**

1. **Set the Video Path:**
   Make sure to specify the correct path to your video file in the `cv.VideoCapture('video')` function before running the code.

2. **Test Motion Detection:**
   As the program runs, green rectangles will appear on the screen where motion is detected, and the start and end times of the motion will be printed to the console.

3. **Exit the Video:**
   To exit the video playback, press the 'q' key.

---

#### **Possible Enhancements**

If you want to further develop this code, consider adding the following features:
- Allow motion detection from multiple video files.
- Use Region of Interest (ROI) to detect motion only in specific areas of the frame.
- Save detected motion or perform other actions when motion is detected.

---

#### **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
