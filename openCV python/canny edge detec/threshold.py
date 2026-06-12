#cv2.threshold 
# cv2.threshold(): applies a fixed-level threshold to each pixel in the image.
# The syntax for cv2.threshold() is as follows: 
# cv2.threshold(src, thresh, maxval, type)
# where:
# - src: the input image.
# - thresh: the threshold value.
# - maxval: the maximum value to use with the cv2.THRESH_BINARY and cv2.THRESH_BINARY_INV thresholding types.
# - type: the thresholding type (e.g., cv2.THRESH_BINARY).

import cv2

image = cv2.imread("median_blurred_image.png",cv2.IMREAD_GRAYSCALE) # read the input image

ret, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # apply thresholding to the image
cv2.imshow("Thresholded Image", thresholded) # display the thresholded image
cv2.waitKey(0) # wait until a key is pressed
cv2.destroyAllWindows() # close the window