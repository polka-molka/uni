import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import cv2

# Sprawdzenie struktury katalogów i liczby obrazów
for root, dirs, files in os.walk('dataset/train/'):
    print(f"Found {len(files)} images in {root}")
for root, dirs, files in os.walk('dataset/validation/'):
    print(f"Found {len(files)} images in {root}")

data_gen = ImageDataGenerator(rescale=1. / 255)

train_generator = data_gen.flow_from_directory(
    'dataset/train/',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)

validation_generator = data_gen.flow_from_directory(
    'dataset/validation/',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(train_generator.num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_generator, epochs=10, validation_data=validation_generator)

model.save('face_classification_model.h5')

# Ładowanie wytrenowanego modelu
model = load_model('face_classification_model.h5')


# Funkcja do ładowania i przetwarzania obrazu
def load_and_preprocess_image(img):
    img_array = cv2.resize(img, (150, 150))
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# Inicjalizacja klasyfikatorów Haar cascade do detekcji twarzy
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Słownik z indeksami klas
class_indices = train_generator.class_indices
class_names = list(class_indices.keys())


# Funkcja do przechwytywania obrazu z kamery, detekcji twarzy i klasyfikacji
def detect_and_classify_faces():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_img = frame[y:y + h, x:x + w]
            img_array = load_and_preprocess_image(face_img)
            predictions = model.predict(img_array)
            predicted_class = class_names[np.argmax(predictions)]

            label = f"{predicted_class}: {np.max(predictions) * 100:.2f}%"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Face Detection and Classification', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Uruchomienie funkcji do przechwytywania obrazu z kamery
detect_and_classify_faces()
