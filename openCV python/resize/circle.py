# ---> cv2.circle(): draws a circle on the image.
# This function allows us to draw a circle on an image by specifying the center coordinates, 
# radius, color, and thickness of the circle.
# The syntax for cv2.circle() is as follows:
# cv2.circle(image, center_coordinates, radius, color, thickness)
# where:
# - image: the input image on which we want to draw the circle.
# - center_coordinates: a tuple representing the center of the circle (x, y).
# - radius: the radius of the circle in pixels.         

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    center_coordinates = (200, 200) # the center of the circle (x, y)
    radius = 50 # the radius of the circle in pixels
    color = (0, 255, 0) # the color of the circle in BGR format (green)
    thickness = 3 # the thickness of the circle outline in pixels

    circle_image=cv2.circle(image, center_coordinates, radius, color, thickness) # draw the circle on the image

    cv2.imshow("Image with Circle", circle_image)
    cv2.imwrite("Python_logo_circle.png", circle_image)  # save the image with the circle to a file
    # display the image with the circle
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window