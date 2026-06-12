# 2 - Rotation and flipping of images: 
# OpenCV provides functions to rotate and flip images.
# ---> cv2.rotate(): rotates the image by a specified angle.
#-------------------------------------------------------------
# ---> cv2.flip(): flips the image horizontally, vertically, or both.
# parameters:
# - image: the input image to be flipped.
# - flipCode: the code that specifies the type of flip to be performed.
#   - 0: flip vertically (around the x-axis).
#   - 1: flip horizontally (around the y-axis).
#   - -1: flip both vertically and horizontally (around both axes).
#-----------------------------------------------------------------
# --> cv2.getRotationMatrix2D(center, angle, scale) 
# # calculates the rotation matrix for a given center, angle, and scale factor.
# parameters:   
# - center: the center of rotation (x, y) coordinates.
# - angle: the angle of rotation in degrees. Positive values mean counter-clockwise rotation, 
# # while negative values mean clockwise rotation.
# - scale: the scale factor for resizing the image. 
# # A value of 1.0 means no scaling, while values less than 1.0 will shrink
#-------------------------------------------------------------
import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:   
    #= = = Rotation of the image ====
    (h,w)= image.shape[:2] # get the height and width of the image
    center = (w//2, h//2) # calculate the center of the image
    m = cv2.getRotationMatrix2D(center, 45, 1.0) # get the rotation matrix for a 45 degree rotation
    rotated = cv2.warpAffine(image, m, (w, h)) # rotate


    #= = = Flipping of the image ====
   # flipped_horizontally = cv2.flip(image, 1) # flip the image horizontally
    flipped_vertically = cv2.flip(image, 0) # flip the image vertically
   # flipped_both = cv2.flip(image, -1) # flip the image both horizontally

    cv2.imshow("flipped Image", flipped_vertically) # display the flipped image




    cv2.imshow("Original Image", image) # display the original image    
    cv2.imshow("Rotated Image", rotated) # display the rotated image
    cv2.imwrite("Python_logo_rotated.png", rotated) # save the rotated image to a file
    cv2.waitKey(0) # wait until a key is pressed
    cv2.destroyAllWindows() # close the windows