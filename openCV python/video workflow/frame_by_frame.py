# cv2.write(): saves an image to a specified file.
# This function allows us to save an image to a file on disk.
# The syntax for cv2.imwrite() is as follows:
# cv2.imwrite(filename, image)
# where:
# - filename: the name of the file to which we want to save the image (e.g., "output.png").
# - image: the image we want to save (the image should be in the form of a NumPy array,
# # which is the standard format for images in OpenCV

import cv2

cap = cv2.VideoCapture ("video.mp4") # open the video file