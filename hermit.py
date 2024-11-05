import matplotlib.pyplot as plt

import numpy as np


def hermite(x_values, y_values, dy_values, x):
    n = len(x_values)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 2 * n))

    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x_values[i]
        Q[2 * i][0] = y_values[i]
        Q[2 * i + 1][0] = y_values[i]
        Q[2 * i + 1][1] = dy_values[i]
        if i != 0:
            Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])

    result = Q[0][0]
    product_term = 1.0
    for i in range(1, 2 * n):
        product_term *= (x - z[i - 1])
        result += Q[i][i] * product_term

    return result


import sympy as sp
from interpolacja import lagrange_interpolation_with_polynomial


def MSE(true_val, fnc_val):
    err = 0
    for i in range(len(true_val)):
        err += (true_val[i] - fnc_val[i]) ** 2
    return err / len(true_val)


def inet():
    x = sp.symbols('x')
    fc = x ** 3 * sp.cos(x)
    func = sp.lambdify(x, fc)
    funcprim = sp.lambdify(x, sp.diff(fc, x))

    epsilon = 1000
    x_points = np.linspace(-10, 10, 10)
    y_points = [func(i) for i in x_points]
    dy_points = [funcprim(i) for i in x_points]
    lag = sp.lambdify(x, lagrange_interpolation_with_polynomial(x_points, y_points))
    x_values = np.linspace(-10, 10, epsilon)
    lagrange = [lag(i) for i in x_values]
    y_values = hermite(x_points, y_points, dy_points, x_values)
    true = [func(i) for i in x_values]

    plt.plot(x_values, y_values, color='#28b463', label='Hermite interpolation', zorder=2)
    plt.plot(x_values, lagrange, color='blue', label='Lagrange interpolation', zorder=1)
    plt.plot(x_values, true, color='black', label=f'${fc}$', zorder=1)
    plt.scatter(x_points, y_points, color='red', label='Data points', zorder=3)

    print(f'Dla lagrange MSE = {MSE(true, lagrange)}')
    print(f'Dla hermita MSE = {MSE(true, y_values)}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Piecewise Hermite Interpolation")
    plt.savefig('/home/tezriem/Documents/UGProjects/MetodyNumeryczne/lab 2/fig.png')


if __name__ == '__main__':
    inet()
