import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model('my_face_recognition_model.h5')

haarcascade_path = 'haarcascade_frontalface_default.xml'
if not os.path.exists(haarcascade_path):
    print(f"Plik klasyfikatora Haar nie został znaleziony: {haarcascade_path}")
    exit()

face_cascade = cv2.CascadeClassifier(haarcascade_path)

mustache_path = r'moustache.png'

if not os.path.exists(mustache_path):
    print(f"Plik wąsów nie został znaleziony: {mustache_path}")
    exit()

mustache = cv2.imread(mustache_path, -1)
if mustache is None:
    print(f"Nie udało się wczytać pliku wąsów: {mustache_path}")
    exit()

def overlay_mustache(face_img, mustache_img):
    mustache_width = int(face_img.shape[1] * 0.6)
    mustache_height = int(mustache_img.shape[0] * (mustache_width / mustache_img.shape[1]))

    mustache_resized = cv2.resize(mustache_img, (mustache_width, mustache_height))

    przesunięcie = 0
    x1 = int(face_img.shape[1] / 2 - mustache_width / 2) + przesunięcie
    y1 = int(face_img.shape[0] * 0.55)
    x2 = x1 + mustache_resized.shape[1]
    y2 = y1 + mustache_resized.shape[0]

    alpha_s = mustache_resized[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        face_img[y1:y2, x1:x2, c] = (alpha_s * mustache_resized[:, :, c] +
                                     alpha_l * face_img[y1:y2, x1:x2, c])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        roi_color = frame[y:y + h, x:x + w]
        face_img = cv2.resize(roi_color, (224, 224))
        face_img = img_to_array(face_img) / 255.0
        face_img = np.expand_dims(face_img, axis=0)

        prediction = model.predict(face_img)
        if prediction[0][0] > 0.5:
            overlay_mustache(roi_color, mustache)

    cv2.imshow('Face with Mustache', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
