# image dimensions and properties: 
# 1 - height: number of rows in the image
# 2 - width: number of columns in the image
# 3 - number of channels: color channels in the image (e.g., 3 for RGB, 4 for RGBA)
# 4 - image.shape: returns a tuple containing the dimensions of the image (height, width, number of channels)


import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not read the image.")
else:
    h,w,c = image.shape
    print(f"Image dimensions:\nheight {h} \n width {w} \n channels {c}")