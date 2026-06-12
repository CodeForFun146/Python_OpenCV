
# 

# 
# 3 - resizing and scaling of images:
# OpenCV provides functions to resize and scale images.
# ---> cv2.resize(): resizes the image to a specified size.
# ---> cv2.resize(): can also be used to scale the image by a specified factor. 
# 

# 
# 5 - Adding text to images:
# OpenCV provides the cv2.putText() function to add text to images.
# This function allows us to specify the text, font, size, color, and position of the text on the image. 
# For example, to add text to an image, we can use the following code:
# cv2.putText(image, "Hello, OpenCV!", (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
# where:
# - image: the input image on which we want to add text.
# - "Hello, OpenCV!": the text we want to add.
# - (x, y): the coordinates of the bottom-left corner of the text on the image.
# - cv2.FONT_HERSHEY_SIMPLEX: the font type for the text.
# - font_scale: the scale factor for the font size.
# - color: the color of the text in BGR format (e.g., (255, 0, 0) for blue).
# - thickness: the thickness of the text strokes       