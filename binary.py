import math
import numpy as np


def float_to_binary(number: float, tolerance: float) -> str:
    if not isinstance(number, float):
        raise ValueError(f'Number need to be float but got: {type(number)}')
    if not isinstance(tolerance, float):
        raise ValueError(f'Tolerance need to be float but got: {type(tolerance)}')


    int_part = math.floor(number)
    frac_part = number - int_part

    int_bin = bin(int_part)[2:] if int_part != 0 else '0'

    frac_bin = ''
    while len(frac_bin) < tolerance:
        frac_part *= 2
        if frac_part >= 1:
            frac_bin += '1'
            frac_part -= 1
        else:
            frac_bin += '0'

    return f'{int_bin}.{frac_bin}'


def find_upper_and_lower_approximation(number: float, tolerance: float) -> tuple[float, str, float, str]:
    if not isinstance(number, float):
        raise ValueError(f'Number need to be float but got: {type(number)}')
    if not isinstance(tolerance, float):
        raise ValueError(f'Tolerance need to be float but got: {type(tolerance)}')
    binary_rep = float_to_binary(number, tolerance)
    _, r = binary_fraction_to_exponent(binary_rep)
    tolerance -= r
    lower_value = math.floor(number * 2 ** tolerance) / 2 ** tolerance
    lower_bin = float_to_binary(lower_value, tolerance)

    upper_value = math.ceil(number * 2 ** tolerance) / 2 ** tolerance
    upper_bin = float_to_binary(upper_value, tolerance)

    return lower_value, lower_bin, upper_value, upper_bin


def main(number: float, tolerance: float):
    if not isinstance(number, float):
        raise ValueError(f'Number need to be float but got: {type(number)}')
    if not isinstance(tolerance, float):
        raise ValueError(f'Tolerance need to be float but got: {type(tolerance)}')
    lower_value, lower_bin, upper_value, upper_bin = find_upper_and_lower_approximation(number, tolerance)
    _ = float_to_binary(number, tolerance)
    print(f"Dolne przybliżenie: {lower_value}, w postaci dwójkowej: {lower_bin}")
    print(f"Górne przybliżenie: {upper_value}, w postaci dwójkowej: {upper_bin}")
    error_lower = abs(number - lower_value)
    error_upper = abs(number - upper_value)
    low = True if error_lower <= error_upper else False
    if low:
        answer = lower_bin
    else:
        answer = upper_bin

    print(f"Liczba {number} w postaci dwójkowej z precyzją {tolerance} bitów: {answer}")
    print(f"Błąd przybliżenia w |x - Fl(x)| = {error_lower if low else error_upper}")


def binary_fraction_to_exponent(binary_fraction: str) -> tuple[float, float]:
    if not isinstance(binary_fraction, str):
        raise ValueError(f"Binary fraction need to be str but got: {type(binary_fraction)}")
    if '.' not in binary_fraction:
        raise ValueError("Liczba musi być w postaci ułamka (z kropką).")

    int_part, frac_part = binary_fraction.split('.')

    binary_number = int_part + frac_part
    if int(binary_number) == 0:
        raise ValueError("Liczba nie może być zerem.")

    if '1' in int_part:
        first_one_index = int_part.index('1')
        exponent = len(int_part) - first_one_index - 1
        mantissa = int_part[first_one_index + 1:] + frac_part
    else:
        first_one_index = frac_part.index('1')
        exponent = -(first_one_index + 1)
        mantissa = frac_part[first_one_index + 1:]

    normalized_mantissa = '1.' + mantissa

    return normalized_mantissa, exponent


if __name__ == '__main__':
    x = 2 / 3
    y = np.float32(x)
    t = 23
    main(y, t)
