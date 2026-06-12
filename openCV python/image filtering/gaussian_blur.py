# cv2.GaussianBlur(): applies a Gaussian filter to an image.
# The syntax for cv2.GaussianBlur() is as follows:
# cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
# where:
# - src: the input image.
# - ksize: the size of the kernel (width, height).
# - sigmaX: the standard deviation in the X direction.
# - sigmaY: the standard deviation in the Y direction.
# - borderType: the type of border to be used (e.g., cv2.BORDER_DEFAULT).

import cv2

image = cv2.imread("image_B.png") # read the input image

if image is None:
    print("Could not read the image.")
else:

 blurred = cv2.GaussianBlur(image, (15, 15), 0) # apply Gaussian blur to the image

 cv2.imshow("Blurred Image", blurred) # display the blurred image

 cv2.imshow("Image", image)
 cv2.imwrite("blurred_image.png", blurred) # save the blurred image to a file
 cv2.waitKey(0) # wait until a key is pressed
 cv2.destroyAllWindows() # close the window