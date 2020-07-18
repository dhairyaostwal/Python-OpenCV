# Python-OpenCV

## ✅ Reading Images

* `imread()` used to read image input
* `imshow()` function shows the output inside a window of name 'image'
* `waitKey()` for making the frame output to wait for some time so we could have a look
* `imwrite()` for copying and making another image
* `destroyAllWindows()` function to quit and destroy all frame-windows

## ✅ Reading Videos

* `VideoCapture(0)` function
* `ret` stores values like true or false
* `frame` captures the frame of the video
* `imshow()` would show the frame inside window named Frame-Test
* Use of `0xFF == ord('q')` which on press of `'q'` key quits the window in which frame was being shown
* Support for adding custom video and convert it into different color output - grayscale etc.
* `isOpened()` function to verify wether video path is correct or not
*  `grayFrame = cv2.cvtColor(frame, cv2.COLOR2GRAY)`
* **NOTE:** Playing inside VSCode Terminal would cause error, better to try on your normal terminal