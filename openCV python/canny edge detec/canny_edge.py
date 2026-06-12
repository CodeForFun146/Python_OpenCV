# canny edge cv2.Canny(): detects edges in an image using the Canny edge detection algorithm.
# The syntax for cv2.Canny() is as follows:
# cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
# where:
# - image: the input image (should be a single-channel 8-bit image, typically a grayscale image).
# - threshold1: the first threshold for the hysteresis procedure (lower threshold).
# - threshold2: the second threshold for the hysteresis procedure (upper threshold).    

import cv2

image = cv2.imread("median_blurred_image.png") # read the input image

edges = cv2.Canny(image, 100, 200) # apply Canny edge detection to the image
cv2.imshow("Canny Edges", edges) # display the edges detected in the image
cv2.imshow("Image", image)
cv2.imwrite("canny_edges.png", edges) # save the edges detected in the image to a file
cv2.waitKey(0) # wait until a key is pressed
cv2.destroyAllWindows() # close the window