import numpy as np


def zadanie4():
    sum_zero = np.float32(0.0)
    for i in range(1, 101):
        sum_zero += np.float32(1 / i)
    print(f'1 - 100: {sum_zero}')

    sum_sto = np.float32(0.0)
    for i in range(100, 1, -1):
        sum_sto += np.float32(1 / i)
    print(f'100 - 1: {sum_sto}')


if __name__ == '__main__':
    zadanie4()
