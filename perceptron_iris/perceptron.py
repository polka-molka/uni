import random

learning_rate = 0.1


def predict(flower_param, bias, weights):
    weight_sum = 0
    for i in range(len(flower_param) - 1):
        weight_sum += float(weights[i]) * float(flower_param[i])

    weight_sum += bias
    if weight_sum > 0:
        return 1
    return 0


def random_weights(set):
    weights = []
    for i in range(len(set[0]) - 1):
        weights.append(random.random())
    return weights


def train(train_set, weights, bias, train_answers):

    predictions = []
    for i in range(len(train_set)):
        prediction = predict(train_set[i], bias, weights)
        predictions.append(prediction)

        error = train_answers[i] - prediction
        for j in range(len(weights)-1):
            weights[j] += learning_rate * error * float(train_set[i][j])

        bias += learning_rate * error
    predictions.append(bias)
    predictions.append(weights)

    return predictions

