import numpy as np
import matplotlib.pyplot as plt

L = 1

def f(x, L):
    return (8*x)/(3*L) - 3*(x/L)**2 + (1/3)*(x/L)**3 - (2/3)*np.sin(np.pi*x/L)

def df(x, L):
    return 8/(3*L) - (6*x)/(L**2) + (x**2)/(L**3) - (2*np.pi)/(3*L)*np.cos(np.pi*x/L)


x = np.linspace(0, L, 100)

plt.plot(x, f(x, L), label="f(x)")
plt.plot(x, df(x, L), label="f'(x)")


plt.grid(True)
plt.legend()

plt.show()