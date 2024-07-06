import csv
import perceptron


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


flag_program = True

train_set = read_the_file("iris_train.txt")
test_set = read_the_file("iris_test.txt")

while flag_program:
    bias = 0
    train_answers = []

    choice = input("Print 'all' to see all the test results or 'new' to test your own data: ")

    if choice == "new":
        flag_input = True
        test_set = list()
        while flag_input:
            new_v = input("Give new values: ")
            test_set.append(new_v.split(","))
            test_set[-1].append("lol")
            if new_v == "stop":
                flag_input = False
        test_set.pop()


    # for i in range(len(train_set[0]) - 1):
    #     to_float(train_set, i)
    #     to_float(test_set, i)

    for i in range(len(train_set)):
        if train_set[i][-1] == "Iris-setosa":
            train_answers.append(1)
        if train_set[i][-1] == "Iris-virginica":
            train_answers.append(0)

    random_weights = perceptron.random_weights(test_set)

    accuracy = 0
    train_total = len(train_set)
    test_total = len(test_set)

    while accuracy < 100:
        right_g = 0
        predictions = perceptron.train(train_set, random_weights, bias, train_answers)
        new_bias = predictions[-2]
        new_weights = predictions[-1]
        predictions.pop()
        predictions.pop()
        for i in range(len(train_answers)):
            if train_answers[i] == predictions[i]:
                right_g += 1
        accuracy = right_g / train_total * 100
        # print(accuracy)

    test_predictions = []
    for i in range(len(test_set)):
        test_predictions.append(perceptron.predict(test_set[i], new_bias, new_weights))

    counter_setosa = 0
    counter_virginica = 0

    if choice == "all":
        for i in range(len(test_set)):
            if test_predictions[i] == 1:
                output = "Iris-setosa"
            else:
                output = "Iris-virginica"
            print(f"Expected: {test_set[i][-1]} -> Output: {output}")
            if test_set[i][-1] == output:
                if output == "Iris-setosa":
                    counter_setosa += 1
                else:
                    counter_virginica += 1
        print("")
        print(f"Accuracy for setosa: {round(counter_setosa / (test_total / 2) * 100, 2)}%")
        print(f"Accuracy for virginica: {round(counter_virginica / (test_total / 2) * 100, 2)}%")
        print(
            f"Total accuracy: {round((counter_setosa + counter_virginica) / test_total * 100, 2)}%")
        print("")
    elif choice == "new":
        print("")
        for i in range(len(test_set)):
            if test_predictions[i] == 1:
                output = "Iris-setosa"
            else:
                output = "Iris-virginica"
            print(f"It seems to be {output}")
        print("")
    elif choice == "exit":
        flag_program = False



# while flag_program:
#     choice = input("Print 'all' to see all the test results or 'new' to test your own data: ")
#     if choice == "new":
#         flag_input = True
#         test_set = list()
#         while flag_input:
#             new_v = input("Give new values: ")
#             test_set.append(new_v.split(","))
#             test_set[-1].append("lol")
#             if new_v == "stop":
#                 flag_input = False
#         test_set.pop()
#
#     for i in range(len(train_set[0]) - 1):
#         to_float(train_set, i)
#         to_float(test_set, i)
#
#     counter_setosa = 0
#     counter_virginica = 0
#
#     total = 15

    # if choice == "all":
    #     for i in range(len(test_set)):
    #
    #         output = list(knn[i].values())
    #         print(f"Expected: {test_set[i][4]} -> Output: {output[0]}")
    #         if test_set[i][4] == output[0]:
    #             if output[0] == "Iris-setosa":
    #                 counter_setosa += 1
    #             else:
    #                 counter_virginica += 1

        # print("")
        # print(f"Accuracy for setosa: {round(counter_setosa / total * 100, 2)}%")
        # print(f"Accuracy for virginica: {round(counter_virginica / total * 100, 2)}%")
        # print(
        #     f"Total accuracy: {round((counter_setosa + counter_virginica) / (total * 2) * 100, 2)}%")
        # print("")

    # elif choice == "new":
    #     for i in range(len(knn)):
    #         output = list(knn[i].values())
    #         print(f"It seems to be {output[i]}")
    #         print("")
    # elif choice == "exit":
    #     flag_program = False
