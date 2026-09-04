import numpy as np
import matplotlib.pyplot as plt

def f(x, l):
    return ((8/3)*(x/l) - 3*(x/l)**2 + (1/3)*(x/l)**3 - (2/3)*np.sin(np.pi*x/l))

def df(x, l):
    return (8/(3*l) - 6*x/l**2 + x**2/l**3 - (2*np.pi)/(3*l) * np.cos(np.pi*x/l))

def g(x, L):
    return 3*L/8 * (3*(x/L)**2 - 1/3 * (x/L)**3 + 2/3*np.sin(np.pi*x/L))


def fixedpoint_metod():
    print("Fixpunkt metod")
    tolerance = 1e-10
    max_iterationer = 1000
    iteration = 0

    fel_fixpunkt = []

    L = 1

    x_inital_guess = 0.8
    x_current = x_inital_guess
    x_next = g(x_current, L)

    while np.abs(x_next - x_current) > tolerance and iteration < max_iterationer:
        x_current = x_next
        x_next = g(x_current, L)
        print(f"i: {iteration}, x: {x_current}, diff: {np.abs(x_next - x_current)}" )
        iteration += 1
        fel_fixpunkt.append(np.abs(x_next - x_current))

    return fel_fixpunkt


def newton_metod():
    print("Newton metod")

    tolerance = 1e-10
    max_iterationer = 1000
    iteration = 0

    fel_newton = []

    L = 1

    x_inital_guess = 0.8
    x_current = x_inital_guess
    x_next = x_current - f(x_current, L)/df(x_current, L)

    while np.abs(x_next - x_current) > tolerance and iteration < max_iterationer:
        x_current = x_next
        x_next = x_current - f(x_current, L)/df(x_current, L)

        print(f"i: {iteration}, x: {x_next}, diff: {np.abs(x_next - x_current)}" )
        iteration += 1
        fel_newton.append(np.abs(x_next - x_current))
    return fel_newton


def plot():
    L = 1
    x = np.linspace(0, L, 500)
    y = f(x, L)

    plt.figure(1)
    plt.plot(x, y)
    plt.title("f(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()


    plt.figure(2)
    fel_fixedpunkt = fixedpoint_metod()
    fel_newton = newton_metod()

    plt.semilogy(fel_fixedpunkt, label="Fixpunkt")
    plt.semilogy(fel_newton, label="Newton")
    plt.legend()
    plt.grid()

    plt.show()

plot()