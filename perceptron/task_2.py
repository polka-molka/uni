import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
from plotka import plot_decision_regions
from reglog import LogisticRegressionGD
#
#
# class SoftmaxRegression(object):
#     def __init__(self, eta=0.05, n_iter=100, random_state=1):
#         self.eta = eta
#         self.n_iter = n_iter
#         self.random_state = random_state
#
#     def fit(self, X, y):
#         rgen = np.random.RandomState(self.random_state)
#         self.classes_ = np.unique(y)
#         self.classifiers_ = {}
#
#         for cls in self.classes_:
#             y_binary = np.where(y == cls, 1, 0)
#             self.classifiers_[cls] = LogisticRegressionGD(eta=self.eta, n_iter=self.n_iter, random_state=self.random_state)
#             self.classifiers_[cls].fit(X, y_binary)
#
#     def predict_proba(self, X):
#         probas = np.zeros((X.shape[0], len(self.classes_)))
#         for idx, cls in enumerate(self.classes_):
#             probas[:, idx] = self.classifiers_[cls].activation(self.classifiers_[cls].net_input(X))
#         return probas / np.sum(probas, axis=1, keepdims=True)
#
#     def predict(self, X):
#         return np.argmax(self.predict_proba(X), axis=1)
#
#
# def main():
#     iris = datasets.load_iris()
#     X = iris.data[:, [2, 3]]
#     y = iris.target
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
#
#     softmax_reg = SoftmaxRegression(eta=0.05, n_iter=1000, random_state=1)
#     softmax_reg.fit(X_train, y_train)
#
#     plot_decision_regions(X=X_train, y=y_train, classifier=softmax_reg)
#     plt.xlabel(r'$x_1$')
#     plt.ylabel(r'$x_2$')
#     plt.legend(loc='upper left')
#
#     plt.show()
#
# if __name__ == '__main__':
#     main()


class MultiClassLogisticRegression(object):
    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        self.classifiers = []

    def fit(self, X, y):
        self.classes = np.unique(y)
        for cls in self.classes:
            y_binary = np.where(y == cls, 1, 0)
            classifier = LogisticRegressionGD(eta=self.eta, n_iter=self.n_iter, random_state=self.random_state)
            classifier.fit(X, y_binary)
            self.classifiers.append(classifier)

    def predict_proba(self, X):
        predictions = np.zeros((X.shape[0], len(self.classes)))
        for i, classifier in enumerate(self.classifiers):
            predictions[:, i] = classifier.activation(classifier.net_input(X))
        exp_scores = np.exp(predictions)
        probabilities = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return probabilities

    def predict(self, X):
        probabilities = self.predict_proba(X)
        return np.argmax(probabilities, axis=1)

def main():
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

    mclr = MultiClassLogisticRegression(eta=0.04, n_iter=500, random_state=1)
    mclr.fit(X_train, y_train)

    y_pred = mclr.predict(X_train)

    accuracy = np.mean(y_pred == y_train)
    print("Dokładność klasyfikacji (trening):", accuracy)

    plot_decision_regions(X=X_train, y=y_train, classifier=mclr)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    main()
