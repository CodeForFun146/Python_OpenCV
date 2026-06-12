# 1 - drawing shapes and text on images:
# OpenCV provides functions to draw various shapes (e.g., lines, rectangles, circles) 
# and text on images. 
# These functions allow us to annotate images, highlight specific regions, 
# or add information to the image.
# ---> cv2.line(): draws a line on the image.
# ---> cv2.rectangle(): draws a rectangle on the image.
# ---> cv2.circle(): draws a circle on the image.
# ---> cv2.putText(): adds text to the image. 

# resize= cv2.resize(image, (new_width, new_height)) 
# # resize the image to a specified size
# scale= cv2.resize(image, None, fx=scale_factor_x, fy=scale_factor_y)
# # scale the image by a specified factor in the x and y directions

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    resized = cv2.resize(image, (300, 300))

    cv2.imshow("Original Image", image) # display the  image

    cv2.imshow("Resized Image", resized) # display the resized image

    cv2.imwrite("Python_logo_resized.png", resized) # save the resized image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the windows