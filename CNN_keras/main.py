from keras.datasets import cifar10
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

(x, y), (_, _) = cifar10.load_data()

class_indices = [4, 1]  # 'deer' and 'automobile'
filtered_indices = [idx for idx, label in enumerate(y) if label in class_indices]
x_filtered = x[filtered_indices]
y_filtered = y[filtered_indices]

y_binary = (y_filtered == 1).astype(int)

x_train, x_test, y_train, y_test = train_test_split(x_filtered, y_binary, test_size=0.7, random_state=42)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

model1 = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model1.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

model2 = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model2.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

model3 = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model3.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model3.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

import matplotlib.pyplot as plt

def plot_history(history, title="Model Performance"):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='train accuracy')
    plt.plot(history.history['val_accuracy'], label='validation accuracy')
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='train loss')
    plt.plot(history.history['val_loss'], label='validation loss')
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

history1 = model1.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))
plot_history(history1, title="Performance of Model 1")

history2 = model2.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))
plot_history(history2, title="Performance of Model 2")

history3 = model3.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))
plot_history(history3, title="Performance of Model 3")