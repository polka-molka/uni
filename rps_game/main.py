import numpy as np
import matplotlib.pyplot as plt

t1 = ['P', 'K', 'N']

wyst = np.array([[2, 4, 0], [0, 0, 4], [4, 0, 2]])

prob_op = np.array([1, 0, 0])

kasa = []
stankasy = 0

n = 150
state = 'P'

for i in range(n):
    if state == 'P':
        pred = np.random.choice(t1, p=wyst[0] / sum(wyst[0]))
        op_akc = np.random.choice(t1, p=prob_op)
        state_index = t1.index(op_akc)
        wyst[0][state_index] += 1
        state = op_akc

        if op_akc == pred:
            stankasy = stankasy + 1
            kasa.append(stankasy)
        elif op_akc == 'N':
            stankasy = stankasy - 1
            kasa.append(stankasy)
        else:
            kasa.append(stankasy)

        print(wyst)
        print(f"State: {state}")
        print(f"Prediction: {pred}")
        print(f"Opponent's action: {op_akc}")
        print("\n")

    if state == 'K':
        pred = np.random.choice(t1, p=wyst[1] / sum(wyst[1]))
        op_akc = np.random.choice(t1, p=prob_op)
        state_index = t1.index(op_akc)
        wyst[1][state_index] += 1
        state = op_akc

        if op_akc == pred:
            stankasy = stankasy + 1
            kasa.append(stankasy)
        elif op_akc == 'P':
            stankasy = stankasy - 1
            kasa.append(stankasy)
        else:
            kasa.append(stankasy)

        print(wyst)
        print(f"State: {state}")
        print(f"Prediction: {pred}")
        print(f"Opponent's action: {op_akc}")
        print("\n")

    if state == 'N':
        pred = np.random.choice(t1, p=wyst[2] / sum(wyst[2]))
        op_akc = np.random.choice(t1, p=prob_op)
        state_index = t1.index(op_akc)
        wyst[2][state_index] += 1
        state = op_akc

        if op_akc == pred:
            stankasy = stankasy + 1
            kasa.append(stankasy)
        elif op_akc == 'K':
            stankasy = stankasy - 1
            kasa.append(stankasy)
        else:
            kasa.append(stankasy)

        print(wyst)
        print(f"State: {state}")
        print(f"Prediction: {pred}")
        print(f"Opponent's action: {op_akc}")
        print("\n")

plt.plot(kasa)
plt.xlabel('Numer rundy')
plt.ylabel('Stan kasy')
plt.title('Zmiana stanu kasy')
plt.show()
