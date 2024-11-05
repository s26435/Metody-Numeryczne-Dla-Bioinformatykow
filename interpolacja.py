import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def lagrange_interpolation_with_polynomial(x_points, y_points):
    x = sp.Symbol('x')
    n = len(x_points)

    if n != len(y_points):
        raise ValueError("len(x)!=len(y)")

    polynomial = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])

        polynomial += y_points[i] * L_i

    return sp.simplify(polynomial)


def sins(x):
    return np.sin(2 * np.pi * x)


def plot_lagrange_polynomials(polynomials, x_points_sets, y_points_sets, func, func_name=r'$sin(2\pi x)$'):
    x = sp.Symbol('x')
    x_values = np.linspace(-1, 1, 500)
    plt.ylim([-1.5, 1.5])

    true_values = func(x_values)
    plt.plot(x_values, true_values, label=func_name, color='black', linewidth=2)

    for i, polynomial in enumerate(polynomials):
        polynomial_func = sp.lambdify(x, polynomial, modules=['numpy'])
        y_values = polynomial_func(x_values)

        mse = np.mean((true_values - y_values) ** 2)
        print(f'MSE dla interpolacji {i + 1}: {mse:.5f}')

        plt.plot(x_values, y_values, label=f'Interpolation {i + 1} (MSE={mse:.5f})')
        plt.scatter(x_points_sets[i], y_points_sets[i], label=f'Points {i + 1}', s=30)

    plt.title('Comparison of Lagrange Interpolation with Different Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.savefig('fig.png')


def zad1():
    how = 6
    x_points_sets = [
        np.array([-0.7, -0.3, 0, 0.8, -0.5, 0.4]),
        np.array([-1, -0.7, 0, 0.7, 1]),
        np.array([random.random() * 2 - 1 for _ in range(how)])
    ]

    polynomials = []
    y_points_sets = []

    for x_points in x_points_sets:
        y_points = np.array([sins(xi) for xi in x_points])
        polynomial = lagrange_interpolation_with_polynomial(x_points, y_points)
        polynomials.append(polynomial)
        y_points_sets.append(y_points)

    plot_lagrange_polynomials(polynomials, x_points_sets, y_points_sets, sins)


def rungego(x):
    return 1 / (1 + 25 * (x ** 2))


def zad2():
    x_points = np.linspace(-1, 1, 7)
    y_points = np.array([rungego(xi) for xi in x_points])
    polynomial = lagrange_interpolation_with_polynomial(x_points, y_points)
    plot_lagrange_polynomials([polynomial], [x_points], [y_points], rungego, func_name=r'$funkcja rungego$')


def monster(x, a=0.5, lim=290):
    b = ((1 + (3 * np.pi / 2)) / a) + 0.1
    ans = 0
    en = 0
    try:
        for dxi in range(lim):
            ans += a ** dxi * np.cos(b ** dxi * np.pi * x)
            en = dxi
        return ans
    except:
        print(f'za duzo iteracji: zakonczono na iteracji {en}')


def zad3():
    x_points = np.linspace(-1, 1, 10)
    y_points = np.array([monster(xi) for xi in x_points])
    polynomial = lagrange_interpolation_with_polynomial(x_points, y_points)
    plot_lagrange_polynomials([polynomial], [x_points], [y_points], monster, func_name='funkcja Monster Welerstrassa')


def ntyczebuszewa(n):
    x = sp.symbols('x')
    return sp.cos(n * sp.cos(x)).expand(trig=True)


def nczybuszewa_polynomial(n):
    x = sp.symbols('x')
    T_n = sp.cos(n * sp.acos(x)).expand(trig=True)
    return sp.lambdify(x, T_n, modules=['numpy'])


def plot_czebyszew_polynomials():
    x_vals = np.linspace(-1, 1, 500)
    plt.figure(figsize=(10, 6))

    for n in range(6):
        T_n = nczybuszewa_polynomial(n)
        y = []
        for x in x_vals:
            y.append(T_n(x))
        y_vals = np.array(y)
        plt.plot(x_vals, y_vals, label=f'T_{n}(x)')

    plt.title("Pierwsze 4 wielomiany Czebyszewa")
    plt.xlabel("x")
    plt.ylabel("T_n(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig('czebuszew.png')


def zad4():
    print(ntyczebuszewa(10))
    plot_czebyszew_polynomials()


def get_roots_czybuszew(n):
    ans = []
    for j in range(0, n + 1):
        ans.append((np.cos(((2 * j + 1) * np.pi) / (2 * (n + 1)))))
    return ans


def zad5():
    n = 7
    x_points = get_roots_czybuszew(n)
    y_points = np.array([rungego(xi) for xi in x_points])
    polynomial = lagrange_interpolation_with_polynomial(x_points, y_points)
    plot_lagrange_polynomials([polynomial], [x_points], [y_points], rungego, func_name=r'$funkcja rungego$')


def wybor(argument):
    switch_dict = {
        1: zad1,
        2: zad2,
        3: zad3,
        4: zad4,
        5: zad5
    }

    return switch_dict.get(argument, lambda: print("nie ma takiej funckji"))()


if __name__ == '__main__':
    func = int(sys.argv[1])
    wybor(func)
