# 4 - cropping:
# Cropping an image involves selecting a specific region of interest (ROI) from the original image.
# This can be done using array slicing in OpenCV.
# For example, to crop a region from the image, we can use the following code:
# cropped_image = image[y1:y2, x1:x2]
# where (x1, y1) and (x2, y2) are the coordinates of 
# the top-left and bottom-right corners of the cropping rectangle, respectively.

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    cropped = image[50:400, 50:600] # crop the image using array slicing (y1:y2, x1:x2)
    cv2.imshow("Original Image", image) # display the original image
    cv2.imshow("Cropped Image", cropped) # display the cropped image
    cv2.imwrite("Python_logo_cropped.png", cropped) # save the cropped image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the windows