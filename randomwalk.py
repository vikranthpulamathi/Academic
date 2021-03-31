import numpy as np
import matplotlib.pyplot as plt
import random as rand


def random1dwalk(n):
    x, y = 0, 0
    xpos, ypos = [0], [0]
    for i in range(n + 1):
        step = rand.uniform(0, 1)
        if step < 0.5:
            x += 1
            y += 1  # moving up
        elif step > 0.5:
            x += 1
            y += -1  # moving down
        xpos.append(x)
        ypos.append(y)

    plt.grid()
    plt.plot(xpos, ypos)
    plt.title("1-D Random Walk ($n = " + str(n) + "$ steps)")
    plt.show()
    return


def random2dwalk(n):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(1, n):
        val = rand.randint(1, 10)
        x[i] = x[i - 1] + rand.uniform(-val, val)
        y[i] = y[i - 1] - rand.uniform(-val, val)

    plt.title("2-D Random Walk ($n = " + str(n) + "$ steps)")
    plt.plot(x, y)
    plt.show()
    return


def randon3dwalk(n):
    r = (np.random.rand(n) * 6).astype("int")
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)
    x[r == 0] = -1
    x[r == 1] = 1
    y[r == 2] = -1
    y[r == 3] = 1
    z[r == 4] = -1
    z[r == 5] = 1
    x = np.cumsum(x)
    y = np.cumsum(y)
    z = np.cumsum(z)
    plt.figure().gca(projection="3d")
    plt.plot(x, y, z)
    plt.title("3-D Random Walk ($n = " + str(n) + "$ steps)")
    plt.show()
    return


list1 = ['[1]One-D', '[2]Two-D', '[3]Three-D']
print(list1)
choice = int(input("Enter a number from above for Random Walk = "))
n = int(input("Enter a huge number = "))  # number of steps

if choice == 1:
    random1dwalk(n)


elif choice == 2:
    random2dwalk(n)


elif choice == 3:
    randon3dwalk(n)
