from unittest import case

import cv2
image_path = input("Enter the path to the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Could not read the image.")
else:  
    action = input("Enter 's' to show the image or 'w' to save the image: ")
    match action:
        case 's':
            print("Image read successfully.")
            cv2.imshow("window title", image) # open the window and display the image
            cv2.waitKey(0) # wait until a key is pressed
            cv2.destroyAllWindows() # close the window
        case 'w':
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, image) # save the image to a file
            print("Image saved successfully.")
        case 'gs':
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the color image to grayscale
            print("Image converted to grayscale successfully.")
            cv2.imshow("window title", gray_image) # open the window and display the image
            cv2.waitKey(0) # wait until a key is pressed
            cv2.destroyAllWindows()