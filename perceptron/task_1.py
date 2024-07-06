# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn import datasets
# from plotka import plot_decision_regions
# from perceptron import Perceptron
#
#
# class PerceptronMultiClass(object):
#
#     def __init__(self, eta=0.01, n_iter=10):
#         self.eta = eta
#         self.n_iter = n_iter
#
#     def fit(self, X, y):
#         self.classes_ = np.unique(y)
#         self.classifiers_ = {}
#
#         for cls in self.classes_:
#             y_binary = np.where(y == cls, 1, -1)
#             self.classifiers_[cls] = Perceptron(eta=self.eta, n_iter=self.n_iter)
#             self.classifiers_[cls].fit(X, y_binary)
#
#     def predict(self, X):
#         predictions = np.zeros((X.shape[0], len(self.classes_)))
#         for idx, cls in enumerate(self.classes_):
#             predictions[:, idx] = self.classifiers_[cls].predict(X)
#         return np.argmax(predictions, axis=1)
#
#
# def main():
#     iris = datasets.load_iris()
#     X = iris.data[:, [2, 3]]
#     y = iris.target
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
#
#     ppn_multi = PerceptronMultiClass(eta=0.1, n_iter=1000)
#     ppn_multi.fit(X_train, y_train)
#
#     plot_decision_regions(X=X_train, y=y_train, classifier=ppn_multi)
#     plt.xlabel('petal length [cm]')
#     plt.ylabel('petal width [cm]')
#     plt.legend(loc='upper left')
#
#     classes_to_plot = [0, 1]  # Choose the classes for which you want to plot decision boundaries
#     for cls in classes_to_plot:
#         weights = ppn_multi.classifiers_[cls].w_
#         slope = -weights[1] / weights[2]
#         intercept = -weights[0] / weights[2]
#         plt.plot(X_train, slope * X_train + intercept, linestyle='--', linewidth=1)
#
#     plt.show()
#
# if __name__ == '__main__':
#     main()
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from perceptron import Perceptron
from plotka import plot_decision_regions


class MultiClassPerceptron(object):
    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter
        self.classifiers = []

    def fit(self, X, y):
        self.classes = np.unique(y)
        for cls in self.classes:
            y_binary = np.where(y == cls, 1, -1)
            classifier = Perceptron(eta=self.eta, n_iter=self.n_iter)
            classifier.fit(X, y_binary)
            self.classifiers.append(classifier)

    def predict(self, X):
        predictions = np.zeros((X.shape[0], len(self.classes)))
        for i, classifier in enumerate(self.classifiers):
            predictions[:, i] = classifier.net_input(X)
        return np.argmax(predictions, axis=1)

from sklearn.metrics import accuracy_score

def main():
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

    mcp = MultiClassPerceptron(eta=0.4, n_iter=1000)
    mcp.fit(X_train, y_train)

    y_pred = mcp.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Dokładność klasyfikacji:", accuracy)

    plot_decision_regions(X=X_train, y=y_train, classifier=mcp)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    main()