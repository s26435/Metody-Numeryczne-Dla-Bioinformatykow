import math
import sys
import numpy as np


def fib():
    a = 1
    b = 1
    while True:
        c = a + b
        if c >= 1000:
            break
        print(c)
        a = b
        b = c


def pierwisatki():
    try:
        a = int(input("Podaj A:"))
        b = int(input("Podaj B:"))
        c = int(input("Podaj C:"))
    except ValueError:
        print(f'A,B,C need to be integer', file=sys.stderr)
        return
    except Exception as err:
        print(f'Unexpected error during user\'s input: {str(err)}', file=sys.stderr)
        return

    ans = []
    if a == 0:
        print(f'A cannot be 0, equation need to be quadratic', file=sys.stderr)
        return

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print(f'Negative delta - equation has no roots', file=sys.stderr)
        return
    if delta == 0:
        ans.append(b / 2 * a)
    else:
        ans.append((b - math.sqrt(delta)) / 2 * a)
        ans.append((b + math.sqrt(delta)) / 2 * a)

    return ans


def zadanie1():
    try:
        if 'pierwisatki' not in globals():
            raise NameError("Required functions 'pierwisatki' are not defined.")
        ans = pierwisatki()
        print(ans)
    except ValueError as e:
        print(e)

def zadanie2():
    try:
        with open('dane.txt', 'r') as file:
            data = [float(line.strip()) for line in file]

        if len(data) == 0:
            print(f'File empty.', file=sys.stderr)
            return

        suma = sum(data)
        average = suma / len(data)
        print(f"Average: {average}")
        wariancja = 0
        for number in data:
            wariancja += math.pow(average - number, 2)
        wariancja = wariancja / (len(data) - 1)
        print(f"Variance: {wariancja}")
        odchylenie = math.sqrt(wariancja) / math.sqrt(len(data))
        print(f"Standard deviation: {odchylenie}")

    except FileNotFoundError:
        print("Error: File 'dane.txt' not found.", file=sys.stderr)
    except ValueError as ve:
        print(f"Value Error: {ve}", file=sys.stderr)
    except ZeroDivisionError:
        print("Error: Division by zero. Check if 'dane.txt' is not empty.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred during statistic calculations: {str(e)}", file=sys.stderr)


def funkcja1(x):
    return np.sqrt(x ** 2 + 1) - 1


def funkcja2(x):
    return np.power(x, 2) / (np.sqrt(x ** 2 + 1) + 1)


def zadanie3():
    try:
        if 'funkcja1' not in globals() or 'funkcja2' not in globals():
            raise NameError("Required functions 'funkcja1' or 'funkcja2' are not defined.")

        print('FUNKCJA 1')
        for y in range(10):
            x = np.float32(np.power(8.0, -y))
            try:
                result = funkcja1(x)
                print(f'f({y})={result}')
            except Exception as e:
                print(f"Error in funkcja1 at f({y}) with x={x}: {e}", file=sys.stderr)

        print('FUNKCJA 2')
        for y in range(30):
            x = np.float32(np.power(8.0, -y))
            try:
                result = funkcja2(x)
                print(f'f({y})={result}')
            except Exception as e:
                print(f"Error in funkcja2 at f({y}) with x={x}: {e}", file=sys.stderr)

    except NameError as ne:
        print(f"Name Error: {ne}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


def re(n: int, x0: float, x1: float):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("The term index 'n' must be a non-negative integer.")

        if not (isinstance(x0, (int, float)) and isinstance(x1, (int, float))):
            raise TypeError("Initial values 'X0' and 'X1' must be numeric (int or float).")

        if n == 0:
            return x0
        elif n == 1:
            return x1

        X_prev = x0
        X_curr = x1
        for i in range(2, n + 1):
            X_next = (13 / 3) * X_curr - (4 / 3) * X_prev
            X_prev = X_curr
            X_curr = X_next

        return X_curr

    except TypeError as te:
        print(f"Type Error: {te}", file=sys.stderr)
    except ValueError as ve:
        print(f"Value Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


def zadanie4():
    try:
        if 're' not in globals():
            raise NameError("Required function 're' is not defined.")

        x = np.float32(1 / 3)
        result_re = re(20, 1.0, x)
        result_pow = np.power(x, 20)

        print(f"Result of re(20, 1.0, x): {result_re}")
        print(f"Result of np.pow(x, 20): {result_pow}")

    except NameError as ne:
        print(f"Name Error: {ne}", file=sys.stderr)
    except ImportError:
        print("Error: 'numpy' module is not imported.", file=sys.stderr)
    except ZeroDivisionError:
        print("Error: Division by zero encountered.", file=sys.stderr)
    except TypeError as te:
        print(f"Type Error: {te}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


def wybor(argument):
    switch_dict = {
        1: zadanie1,
        2: zadanie2,
        3: zadanie3,
        4: zadanie4,
    }

    return switch_dict.get(argument, lambda: print("nie ma takiej funckji"))()


if __name__ == '__main__':
    wybor(int(sys.argv[1]))
