import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math
import matplotlib.animation as animation

def f(x):
    return np.cos(x)


def so_ode(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    y = np.zeros(len(x))
    yd = np.zeros(len(x))
    err = np.zeros(len(x))
    y[0] = 1
    yd[0] = 0
    for i in range(len(x) - 1):
        y[i + 1] = y[i] + h * yd[i]
        yd[i + 1] = yd[i] - h * y[i]
        err[i] = abs((f(x[i]) - y[i]) / f(x[i]))
    plt.grid()
    plt.plot(x, f(x))
    plt.plot(x, y, "r*")
    plt.plot(x, err)
    plt.legend(['f(x)', 'Computed'])
    plt.show()
    return y


# so_ode(0, 2*np.pi, 100)



def mode1(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = -(b/m)*theta2 - (g/l)*np.sin(theta1)
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt


# damping coefficient
b = 0
# acceleration due to gravity
g = 9.81
# length of string
l = 1
# mass of bob
m = 1

# initial condition
theta_0 = [0, 1]
# time points
t = np.linspace(0, 10, 150)
# solving ODE by function call
theta = odeint(mode1, theta_0, t, args=(b, g, l, m))
# plotting results for transient behavior
plt.figure()
plt.plot(t, theta[:, 0], 'b-')
plt.plot(t, theta[:, 1], 'r--')
plt.plot(theta[:, 0], theta[:, 1])
plt.ylabel('Plot')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()

# animation
fig = plt.figure(figsize=(5, 5), facecolor='w')
ax = fig.add_subplot(1, 1, 1)
plt.rcParams['font.size'] = 15

lns = []
for i in range(len(theta)):
    ln, = ax.plot([0, np.sin(theta[i, 0])], [0, -np.cos(theta[i, 0])], color='k', lw=2)
    bob, = ax.plot([np.sin(theta[i, 0])], [-np.cos(theta[i, 0])], 'o', markersize=20, color='r')
    tm = ax.text(-0.9, 0.25, 'Time = %0.1fs'%t[i])
    lns.append([ln, bob, tm])

ax.set_aspect('equal', 'datalim')

ani = animation.ArtistAnimation(fig, lns, interval=50)
fn = 'Pendulum Animation'
ani.save(fn+'.mp4', writer='ffmpeg', fps=1000/100)
