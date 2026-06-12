#cv2.putText(): adds text to the image.
# This function allows us to add text to an image by specifying the text, font, size, color, and position of the text on the image.
# The syntax for cv2.putText() is as follows:
# cv2.putText(image, "Hello, OpenCV!", (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
# where:
# - image: the input image on which we want to add text.
# - "Hello, OpenCV!": the text we want to add.
# - (x, y): the coordinates of the bottom-left corner of the text on the image.
# - cv2.FONT_HERSHEY_SIMPLEX: the font type for the text.
# - font_scale: the scale factor for the font size.
# - color: the color of the text in BGR format (e.g., (255, 0, 0) for blue).
# - thickness: the thickness of the text strokes    

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:   
    text = "Hello, OpenCV!" # the text we want to add
    position = (50, 50) # the coordinates of the bottom-left corner of the text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX # the font type for the text
    font_scale = 1 # the scale factor for the font size
    color = (255, 0, 0) # the color of the text in BGR format (blue)
    thickness = 2 # the thickness of the text strokes

    text_image=cv2.putText(image, text, position, font, font_scale, color, thickness) # add text to the image

    cv2.imshow("Image with Text", text_image)
    cv2.imwrite("Python_logo_text.png", text_image)  # save the image with the text to a file
    # display the image with the text
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window