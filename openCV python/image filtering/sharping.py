#cv2.filter2D(): applies a custom linear filter to an image.
# The syntax for cv2.filter2D() is as follows:
# cv2.filter2D(src, ddepth, kernel)
# where:
# - src: the input image.
# - ddepth: the desired depth of the output image (e.g., cv2.CV_8U for 8-bit unsigned integers).
# - kernel: the convolution kernel (a 2D array that defines the filter to be applied to the image).

import cv2
import numpy as np

image = cv2.imread("image_B.png") # read the input image

if image is None:
    print("Could not read the image.")
else:   
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]) # define a custom kernel (cross-shaped)
    

    sharpened = cv2.filter2D(image, -1, kernel) # apply the filter to the image

    cv2.imshow("Sharpened Image", sharpened) # display the sharpened image

    cv2.imshow("Image", image)
    cv2.imwrite("sharpened_image.png", sharpened) # save the sharpened image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window