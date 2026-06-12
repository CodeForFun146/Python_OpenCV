#cv2.line(image, start_point, end_point, color, thickness)
#- image: the input image on which we want to draw the line.
#- start_point: a tuple representing the starting coordinates of the line (x1, y1).
#- end_point: a tuple representing the ending coordinates of the line (x2, y2).
#- color: the color of the line in BGR format (e.g., (255, 0, 0) for blue).
#- thickness: the thickness of the line in pixels.

import cv2

image = cv2.imread("resize/Python-1_logo.png")

if image is None:
    print("Could not read the image.")
else:
    path1 = (50, 50) # starting coordinates of the line (x1, y1)
    path2 = (400, 400) # ending coordinates of the line (x2, y2)
    color = (255, 0, 0) # color of the line in BGR format (blue)
    thickness = 5 # thickness of the line in pixels
    line_image=cv2.line(image, path1, path2, color, thickness) # draw the line on the image
    
    cv2.imshow("Image with Line", line_image) 
    cv2.imwrite("Python-1_logo_line.png", line_image)  # save the image with the line to a file
    # display the image with the line
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window