# 1 - gray scale image: an image that contains only intensity information, without color. 
# It is represented as a single channel (grayscale) image, where each pixel value represents the intensity of light at that point. 
# Grayscale images are often used in image processing tasks where color information is not necessary, 
# such as edge detection or object recognition.

# 2 - cv2.cvtColor() function is used to convert an image from one color space to another. 
# To convert a color image to grayscale, we can use the following code:
# parameters:
# -->  source image: the input color image that we want to convert to grayscale.
# -->  color conversion code: a code that specifies the type of color conversion we want
# e.g cv2.COLOR_BGR2GRAY: converts a BGR color image to grayscale.

import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the color image to grayscale
    print("Image converted to grayscale successfully.")
    cv2.imshow("Grayscale Image", gray_image) # display the grayscale image
    cv2.imwrite("Python_logo_gray.png", gray_image) # save the grayscale image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window