











import cv2

image = cv2.imread("Python_logo.png")

# cv2.imwrite("Python_logo_copy.png", image) 
# # save the image to a file 
# # two parameters: filename and image  

if image is None:
    print("Could not read the image.")
else:
    print("Image read successfully.")
    cv2.imshow("window title", image) # open the window and display the image
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the window
