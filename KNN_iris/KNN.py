from math import sqrt


def euclidean_distance(vector, data):
    distance = 0.0
    for i in range(len(vector) - 1):
        distance += (vector[i] - data[i]) ** 2
    return sqrt(distance)


def find_nearest_neighbors(train_set, vector, num):
    distances = list()
    for data in train_set:
        distance = euclidean_distance(vector, data)
        distances.append((data[4], distance))
    distances.sort(key=lambda a: a[1])
    neighbors = list()
    for i in range(num):
        neighbors.append(distances[i])
    return neighbors


def predict(train_set, vector, num):
    neighbors = find_nearest_neighbors(train_set, vector, num)
    final = [row[-1] for row in neighbors]
    prediction = max(set(final), key=final.count)
    # if [row[-1] for row in neighbors] == prediction:
    #     flower = str([row[0] for row in neighbors])

    for i in range(len(neighbors)):
        if neighbors[i][-1] == prediction:
            flower = neighbors[i][0]
    pair = {prediction: flower}
    return pair


def knn(train_set, test_set, num):
    predictions = list()
    for test_vector in test_set:
        final = predict(train_set, test_vector, num)
        predictions.append(final)
    return (predictions)
