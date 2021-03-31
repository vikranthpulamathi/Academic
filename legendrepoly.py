import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

N = 1000
xvals = np.linspace(-1, 1, N)


def Legendre(x, n):
    leg = legendre(n)
    P_n = leg((x))
    return P_n

for i in range(0, 6):
    func = Legendre(xvals, i)
    plt.plot(xvals, func)

plt.grid()
plt.title("4 Legendre P_n(cos(x))")
plt.show()
