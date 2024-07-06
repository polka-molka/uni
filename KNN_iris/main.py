import csv

import KNN


def read_the_file(file):
    data_set = list()
    with open(file, "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            data_set.append(row)
    return data_set


def to_float(data_set, column):
    for row in data_set:
        row[column] = float(row[column].strip())


flag = True

while flag:
    train_set = read_the_file("iris_train.txt")
    test_set = read_the_file("iris_test.txt")
    choice = input("Print 'all' to see all the test results or 'new' to test your own data: ")
    if choice == "new":
        test_set = list()
        new_v = input("Give new values: ")
        test_set.append(new_v.split(","))
        test_set[0].append("lol")

    for i in range(len(train_set[0]) - 1):
        to_float(train_set, i)
        to_float(test_set, i)

    k = 12

    knn = KNN.knn(train_set, test_set, k)

    counter_setosa = 0
    counter_versicolor = 0
    counter_virginica = 0

    total = 15

    if choice == "all":
        for i in range(len(test_set)):

            output = list(knn[i].values())
            print(f"Expected: {test_set[i][4]} -> Output: {output[0]}")
            if test_set[i][4] == output[0]:
                if output[0] == "Iris-versicolor":
                    counter_versicolor += 1
                elif output[0] == "Iris-setosa":
                    counter_setosa += 1
                else:
                    counter_virginica += 1

        print("")
        print(f"Accuracy for versicolor: {round(counter_versicolor / total * 100, 2)}%")
        print(f"Accuracy for setosa: {round(counter_setosa / total * 100, 2)}%")
        print(f"Accuracy for virginica: {round(counter_virginica / total * 100, 2)}%")
        print(
            f"Total accuracy: {round((counter_setosa + counter_virginica + counter_versicolor) / (total * 3) * 100, 2)}%")
        print("")

    elif choice == "new":
        output = list(knn[0].values())
        print(f"It seems to be {output[0]}")
        print("")
    elif choice == "exit":
        flag = False
