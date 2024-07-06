import cv2
import os

cap = cv2.VideoCapture(0)
count = 0

if not os.path.exists('data'):
    os.makedirs('data')

while count < 100:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Collecting your face data', frame)
    cv2.imwrite(f'data/{count}.jpg', frame)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
