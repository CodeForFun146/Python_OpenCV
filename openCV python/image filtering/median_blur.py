#cv2.medianblur(): applies a median blur filter to an image.
# The syntax for cv2.medianBlur() is as follows:
# cv2.medianBlur(src, ksize)
# where:
# - src: the input image.
# - ksize: the size of the kernel (must be a positive odd integer, e.g., 3, 5, 7).
import cv2

image=cv2.imread("median.jpg") # read the input image

if image is None:
    print("Could not read the image.")
else:
    blurred = cv2.medianBlur(image, 11) # apply median blur to the image

    cv2.imshow("Blurred Image", blurred) # display the blurred image

    cv2.imshow("Image", image)
    cv2.imwrite("median_blurred_image.png", blurred) # save the blurred image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window