import numpy as np
import matplotlib.pyplot as plt


def f(x, L):
    return (
        (8/3)*(x/L)
        - 3*(x/L)**2
        + (1/3)*(x/L)**3
        - (2/3)*np.sin(np.pi*x/L)
    )

def df(x, L):
    return (
        8/(3*L)
        - 6*x/L**2
        + x**2/L**3
        - (2*np.pi)/(3*L) * np.cos(np.pi*x/L)
    )

def g(x, L):
    return (3*L/8) * (
        3*(x/L)**2
        - (1/3)*(x/L)**3
        + (2/3)*np.sin(np.pi*x/L)
    )


def fixedpoint_metod(L, x_initial_guess, tolerance, max_iterationer):
    print("Fixpunktsmetod")

    iteration = 0
    fel = []

    x_current = x_initial_guess
    x_next = g(x_current, L)

    while abs(x_next - x_current) > tolerance and iteration < max_iterationer:
        x_current = x_next
        x_next = g(x_current, L)

        diff = abs(x_next - x_current)
        fel.append(diff)

        print(f"i: {iteration}, x: {x_next}, diff: {diff}")

        iteration += 1

    return x_next, fel


def newton_metod(L, x_initial_guess, tolerance, max_iterationer):
    print("Newtons metod")

    iteration = 0
    fel = []

    x_current = x_initial_guess
    x_next = x_current - f(x_current, L) / df(x_current, L)

    while abs(x_next - x_current) > tolerance and iteration < max_iterationer:
        x_current = x_next
        x_next = x_current - f(x_current, L) / df(x_current, L)

        diff = abs(x_next - x_current)
        fel.append(diff)

        print(f"i: {iteration}, x: {x_next}, diff: {diff}")

        iteration += 1

    return x_next, fel


def plot_funktion():
    L = 1

    x = np.linspace(0, L, 500)
    y = f(x, L)

    plt.figure()
    plt.plot(x, y)
    plt.axhline(0)
    plt.title("f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()


def plot_konvergens(fel_fixpunkt, fel_newton):
    plt.figure()

    plt.semilogy(fel_fixpunkt, label="Fixpunkt")
    plt.semilogy(fel_newton, label="Newton")

    plt.xlabel("Iteration")
    plt.ylabel("|x_next - x_current|")
    plt.legend()
    plt.grid()


tolerance = 1e-10
max_iterationer = 1000

# Uppgift 1a
plot_funktion()

# Uppgift 1c
x_fix, fel_fix = fixedpoint_metod(
    L = 1,
    x_initial_guess=0.8,
    tolerance=tolerance,
    max_iterationer=max_iterationer
)

# Uppgift 1d
x_newton, _ = newton_metod(
    L = 1,
    x_initial_guess=0.3,
    tolerance=tolerance,
    max_iterationer=max_iterationer
)

# Uppgift 1e
x_fix, fel_fix = fixedpoint_metod(
    L = 1,
    x_initial_guess=0.8,
    tolerance=tolerance,
    max_iterationer=max_iterationer
)

x_newton, fel_newton = newton_metod(
    L = 1,
    x_initial_guess=0.8,
    tolerance=tolerance,
    max_iterationer=max_iterationer
)

plot_konvergens(fel_fix, fel_newton)

plt.show()
