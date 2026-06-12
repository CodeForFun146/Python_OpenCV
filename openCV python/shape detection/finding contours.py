#cv2.finding contours:
# This function is used to find contours in a binary image.
# The syntax for cv2.findContours() is as follows:
# cv2.findContours(image, mode, method)
# where:
# - image: the input image (must be a binary image).
# - mode: the contour retrieval mode.
# - method: the contour approximation method.

import cv2


image = cv2.imread('shape detection/yellow-triangle.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

