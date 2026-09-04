import numpy as np
import matplotlib.pyplot as plt



def f(x, l):
    return (8*x)/(3*l) - 3*(x/l)**2 + (1/3)*(x/l)**3 - (2/3)*np.sin(np.pi*x/l)


def df(x, l, lim=1e-6):
    return (f(x + lim, l) - f(x - lim, l)) / (2*lim)


def newton(x, l, tolerance=1e-10):
    denominator = df(x, l)

    if np.abs(denominator) < tolerance:
        raise ValueError("Derivatan är för nära 0")

    return x - f(x, l) / denominator


def fixpoint(x_n, l):
    return (3*l/8) * (
        3*(x_n/l)**2
        - (1/3)*(x_n/l)**3
        + (2/3)*np.sin(np.pi*x_n/l)
    )


def fixpoint_loop(x, l, tolerance, max_iter):
    x_next = fixpoint(x, l)
    i = 0

    while np.abs(x_next - x) > tolerance and i < max_iter:
        x = x_next
        x_next = fixpoint(x, l)

        print(i + 1, x_next)

        i += 1

    if i == max_iter:
        print("Fixpunktsmetoden nådde max antal iterationer")
    else:
        print(f"Fixpunktsmetoden konvergerade efter {i} iterationer")

    print(f"Rot: {x_next}")


def newton_loop(x, l, tolerance, max_iter):
    for i in range(max_iter):
        x_next = newton(x, l)

        print(f"x_next: {x_next}, x_prev: {x}")

        if np.abs(x_next - x) < tolerance:
            print(f"Newtons metod konvergerade efter {i + 1} iterationer")
            print(f"Rot: {x_next}")
            return

        x = x_next

    print("Newtons metod nådde max antal iterationer")
    print(f"Rot: {x}")


def main_loop():
    x_0 = 0.8
    l = 1
    tolerance = 1e-10
    max_iter = 1000

    print("Fixpunktsmetoden:")
    fixpoint_loop(x_0, l, tolerance, max_iter)

    print("\nNewtons metod:")
    newton_loop(x_0, l, tolerance, max_iter)


def graph():
    return 


main_loop()