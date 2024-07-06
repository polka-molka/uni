import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

from main import train_generator

# Wczytanie wytrenowanego modelu
model = load_model('face_classification_model.h5')

# Funkcja do ładowania i przetwarzania obrazu
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # Dostosuj do rozmiaru wejściowego modelu
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizacja obrazu
    return img_array

# Ścieżka do nowego obrazu do testowania
test_image_path = 'dataset/test/emma_test1.jpg'

# Ładowanie i przetwarzanie obrazu
img_array = load_and_preprocess_image(test_image_path)

# Przewidywanie klasy obrazu
predictions = model.predict(img_array)

# Wyświetlenie wyników
class_indices = train_generator.class_indices
class_names = list(class_indices.keys())
predicted_class = class_names[np.argmax(predictions)]

print(f"Predicted class: {predicted_class}")
print(f"Predicted probabilities: {predictions}")

