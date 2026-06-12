# cv2.bitwise_not(): performs a bitwise NOT operation on an image.
# This function is used to invert the pixel values of an image.
# The syntax for cv2.bitwise_not() is as follows:
# cv2.bitwise_not(src, dst, mask)
# where:
# - src: the input image.
# - dst: the output image (optional).
# - mask: an optional mask to specify which pixels to operate on (must be a single-channel 8-bit image).



import cv2
import numpy as np

image1 = np.zeros((300, 300), dtype=np.uint8) # create a black image
image2 = np.zeros((300, 300), dtype=np.uint8) # create another black image

cv2.rectangle(image1, (100, 100), (250, 250), 255, -1) # draw a white rectangle on the first image
cv2.circle(image2, (150, 150), 100, 255, -1) # draw a white circle on the second image


bitwise_not_result = cv2.bitwise_not(image1) # perform bitwise NOT operation on the first image

cv2.imshow("Image 1", image1) # display the first image
cv2.imshow("Image 2", image2) # display the second image
cv2.imshow("Bitwise NOT Result", bitwise_not_result) # display the result of the bitwise NOT operation


cv2.waitKey(0) # wait until a key is pressed
cv2.destroyAllWindows() # close the windows