import cv2
import numpy as np

image = cv2.imread('tray1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (3, 3), 0)

edges = cv2.Canny(blurred, 20, 80)
dilated = cv2.dilate(edges, None, iterations=2)
eroded = cv2.erode(dilated, None, iterations=1)

blurred = cv2.GaussianBlur(dilated, (9, 9), 0)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.18, minDist=40, param1=50,
                           param2=43, minRadius=28, maxRadius=43)

contours, hierarchy = cv2.findContours(eroded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

gr_counter = 0
gr_area = 0

zl_counter = 0
zl_area = 0

largest_contour = max(contours, key=cv2.contourArea)

x, y, w, h = cv2.boundingRect(largest_contour)

tray_area = w * h

cv2.drawContours(image, [largest_contour], -1, (255, 0, 0), 2)

on_tray = 0
outside_tray = 0

tray_x, tray_y, tray_w, tray_h = x, y, w, h
image_height, image_width, _ = image.shape

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, radius) in circles:
        if 37 <= radius < 50:
            if tray_x <= x <= tray_x + tray_w and tray_y <= y <= tray_y + tray_h:
                on_tray += 5
            else:
                outside_tray += 5
            cv2.circle(image, (x, y), radius, (0, 255, 0), 2)
            cv2.putText(image, '5zl', (x - 20, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            zl_counter += 1
            zl_area = np.pi * (radius ** 2)
        elif radius < 37:
            if tray_x <= x <= tray_x + tray_w and tray_y <= y <= tray_y + tray_h:
                on_tray += 0.05
            else:
                outside_tray += 0.05
            cv2.circle(image, (x, y), radius, (0, 0, 255), 2)
            cv2.putText(image, '5gr', (x - 20, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            gr_counter += 1
            gr_area = np.pi * (radius ** 2)

cv2.putText(image, f'Zl: {zl_counter}, {round(zl_area)}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(image, f'Gr: {gr_counter}, {round(gr_area)}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(image, f'Tray: {round(tray_area)}', (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(image, f'On: {on_tray}, out: {round(outside_tray, 3)}', (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

resized_image = cv2.resize(image, (300, 400))

cv2.imshow('Detected Coins', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
