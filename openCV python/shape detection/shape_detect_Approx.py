# cv2.approxPolyDP():
# Approximate a contour shape to another shape with fewer vertices.
# cv2.approxPolyDP(curve, epsilon, closed)
# - curve: the input contour.
# - epsilon: the approximation accuracy.
# - closed: whether the curve is closed.

import os
import cv2

image_path = input('Enter the path of the image: ').strip()
if not os.path.isfile(image_path):
    raise SystemExit(f'Image file not found: {image_path}')

image = cv2.imread(image_path)
if image is None:
    raise SystemExit('Unable to open image. Check the file path and image format.')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    if area < 200:
        continue

    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    corners = len(approx)

    if corners == 3:
        shape_name = 'Triangle'
    elif corners == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = 'Square'
        else:
            shape_name = 'Rectangle'
    elif corners == 5:
        shape_name = 'Pentagon'
    elif corners == 6:
        shape_name = 'Hexagon'
    elif corners > 6:
        shape_name = 'Circle'
    else:
        shape_name = 'Unknown'

    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    x, y, w, h = cv2.boundingRect(approx)
    label_position = (x, y - 10 if y - 10 > 10 else y + h + 20)
    cv2.putText(image, shape_name, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow('Approximated Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
