# cv2.bitwise_and(): performs a bitwise AND operation between two images or an image and a mask.
# This function is used to combine two images or to apply a mask to an image.
# The syntax for cv2.bitwise_and() is as follows:
# cv2.bitwise_and(src1, src2, dst, mask)
# where:
# - src1: the first input image.
# - src2: the second input image (must be the same size and type as src1).
# - dst: the output image (optional).
# - mask: an optional mask to specify which pixels to operate on (must be a single-channel 8-bit image).




import cv2
import numpy as np

image1 = np.zeros((300, 300), dtype=np.uint8) # create a black image
image2 = np.zeros((300, 300), dtype=np.uint8) # create another black image

cv2.rectangle(image1, (100, 100), (250, 250), 255, -1) # draw a white rectangle on the first image
cv2.circle(image2, (150, 150), 100, 255, -1) # draw a white circle on the second image

bitwise_and_result = cv2.bitwise_and(image1, image2) # perform bitwise AND operation between the two images


cv2.imshow("Image 1", image1) # display the first image
cv2.imshow("Image 2", image2) # display the second image
cv2.imshow("Bitwise AND Result", bitwise_and_result) # display the result of the bitwise AND operation

cv2.waitKey(0) # wait until a key is pressed
cv2.destroyAllWindows() # close the windows