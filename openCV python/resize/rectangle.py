#cv2.rectangle() function is used to draw a rectangle on an image.
# The syntax for cv2.rectangle() is as follows:
# cv2.rectangle(image, start_point, end_point, color, thickness)
# where:
# - image: the input image on which we want to draw the rectangle.
# - start_point: a tuple representing the top-left corner of the rectangle (x1, y1).
# - end_point: a tuple representing the bottom-right corner of the rectangle (x2, y2).
# - color: the color of the rectangle in BGR format (e.g., (255, 0, 0) for blue).
# - thickness: the thickness of the rectangle border in pixels. If thickness is set to -1, 
# the rectangle will be filled with the specified color.           

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    path1 = (50, 50) # top-left corner of the rectangle (x1, y1)
    path2 = (400, 400) # bottom-right corner of the rectangle (x2, y2)
    color = (255, 0, 0) # color of the rectangle in BGR format (blue)
    thickness = 5 # thickness of the rectangle border in pixels
    rectangle_image=cv2.rectangle(image, path1, path2, color, thickness) # draw the rectangle on the image

    cv2.imshow("Image with Rectangle", rectangle_image)
    cv2.imwrite("Python_logo_rectangle.png", rectangle_image)  # save the image with the rectangle to a file
    # display the image with the rectangle
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window