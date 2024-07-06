from keras import layers, models
from keras.datasets import mnist
from keras.utils import to_categorical
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

input_shape = (28, 28, 1)
encoder_input = layers.Input(shape=input_shape)
x = layers.Conv2D(16, (3, 3), padding='same', activation='relu')(encoder_input)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(8, (3, 3), padding='same', activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(4, (3, 3), padding='same', activation='relu')(x)

encoder_output = layers.Flatten()(x)
encoder = models.Model(encoder_input, encoder_output, name="encoder")

x = layers.Reshape((7, 7, 4))(encoder_output)
x = layers.Conv2DTranspose(8, (3, 3), padding='same', activation='relu')(x)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2DTranspose(16, (3, 3), padding='same', activation='relu')(x)
x = layers.UpSampling2D((2, 2))(x)
decoder_output = layers.Conv2D(1, (3, 3), padding='same', activation='sigmoid')(x)

autoencoder = models.Model(encoder_input, decoder_output, name="autoencoder")
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(train_images, train_images, epochs=5, batch_size=64)

encoded_images = encoder.predict(train_images)

encoded_input = layers.Input(shape=(196,))
x = layers.Dense(64, activation='relu')(encoded_input)
classifier_output = layers.Dense(10, activation='softmax')(x)
classifier = models.Model(encoded_input, classifier_output, name="classifier")

num_samples = int(0.1 * len(train_labels))
indices = np.random.choice(len(train_labels), num_samples, replace=False)
partial_train_images = encoded_images[indices]
partial_train_labels = to_categorical(train_labels[indices], 10)

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
classifier.fit(partial_train_images, partial_train_labels, epochs=10, batch_size=64)

test_encoded_images = encoder.predict(test_images)
test_labels_categorical = to_categorical(test_labels, 10)
test_loss, test_acc = classifier.evaluate(test_encoded_images, test_labels_categorical)
print(f"Test accuracy: {test_acc}")

kmeans = KMeans(n_clusters=10, random_state=0)
kmeans.fit(encoded_images)
cluster_centers = kmeans.cluster_centers_

def assign_labels(data, centers):
    labels = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        distances = np.linalg.norm(data[i] - centers, axis=1)
        labels[i] = np.argmin(distances)
    return labels

cluster_labels = assign_labels(encoded_images, cluster_centers)
accuracy = accuracy_score(train_labels, cluster_labels)
print(f"Clustering accuracy: {accuracy}")
