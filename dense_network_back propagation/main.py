import numpy as np

def load_data(file_name):
    data = np.loadtxt(file_name)
    X = data[:, 0].reshape(-1, 1)
    y = data[:, 1].reshape(-1, 1)
    return X, y

def split_data(X, y, test_ratio=0.2):
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    test_size = int(len(indices) * test_ratio)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], y[train_indices], X[test_indices], y[test_indices]

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, activation='tanh'):
        self.input_size = input_size + 1
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.activation = activation

        self.W1 = np.random.randn(self.input_size, self.hidden_size) * 0.1
        self.W2 = np.random.randn(self.hidden_size, self.output_size) * 0.1

    def _activate(self, x):
        if self.activation == 'tanh':
            return np.tanh(x)
        elif self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        elif self.activation == 'relu':
            return np.maximum(0, x)
        else:
            raise ValueError("Unsupported activation function")

    def _activate_derivative(self, x):
        if self.activation == 'tanh':
            return 1 - np.tanh(x) ** 2
        elif self.activation == 'sigmoid':
            return x * (1 - x)
        elif self.activation == 'relu':
            return np.where(x > 0, 1, 0)
        else:
            raise ValueError("Unsupported activation function")

    def forward(self, x):
        x = np.append(x, 1)
        self.z1 = np.dot(x, self.W1)
        self.a1 = self._activate(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        output = self.z2
        return output

    def backward(self, x, y, output, learning_rate):
        output_error = y - output
        output_delta = output_error

        z1_error = output_delta.dot(self.W2.T)
        z1_delta = z1_error * self._activate_derivative(self.a1)

        x = np.append(x, 1)

        output_delta_reshaped = output_delta.reshape(-1, 1)
        self.W2 += learning_rate * self.a1.reshape(-1, 1).dot(output_delta_reshaped.T)

        self.W1 += learning_rate * x.reshape(-1, 1).dot(z1_delta.reshape(1, -1))

    def train_batch(self, X, y, learning_rate=0.01, epochs=1000):
        for epoch in range(epochs):
            for x, target in zip(X, y):
                output = self.forward(x)
                self.backward(x, target, output, learning_rate)

    def predict(self, X):
        outputs = np.array([self.forward(x) for x in X])
        return outputs.squeeze()

X, y = load_data('Dane/dane1.txt')

X_train, y_train, X_test, y_test = split_data(X, y)

nn = NeuralNetwork(input_size=1, hidden_size=10, output_size=1, activation='tanh')

nn.train_batch(X_train, y_train, learning_rate=0.01, epochs=5000)

predictions = nn.predict(X_test)
mse = np.mean((predictions - y_test.squeeze()) ** 2)
print("Test predictions:", predictions)
print("Mean Squared Error:", mse)
