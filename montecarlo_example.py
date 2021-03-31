import numpy as np
import random
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 2000


def f(x):
    return np.sin(x)

areas = []
for i in range(N):
    xrand = np.zeros(N)
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a, b)
    integral = 0
    for i in range(N):
        integral += f(xrand[i])
    answer = (b-a)/N * integral
    areas.append(answer)

plt.title("Distribution of Areas - Monte Carlo Integration")
plt.xlabel("Areas")
plt.hist(areas, bins=50, ec='black')
plt.savefig("montecarlo.png", format="png")

