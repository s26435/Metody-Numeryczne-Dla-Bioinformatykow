# Metody Numeryczne dla Bioinformatyków

[English version here](#numerical-methods-for-bioinformatics)


# Zajęcia nr 1: <br>
   Plik: ```binary.py``` <br>
   Operacje zamiany liczb zmiennoprzecinkowych dziesiętnych na binarne i odwrotnie, wraz z pokazaniem błędu podczas zamiany
    * ```float_to_binary```: Konwertuje liczbę zmiennoprzecinkową na format binarny z precyzją określoną przez tolerancję. 
    * ```find_upper_and_lower_approximation```: Znajduje i zwraca najbliższe przybliżenia binarne (górne i dolne) danej liczby zmiennoprzecinkowej w ramach określonej tolerancji.
    * ```binary_fraction_to_exponent```: Przekształca ułamek binarny na znormalizowaną notację naukową, zwracając mantysę i wykładnik
    <p>Skrypt oblicza i wyświetla reprezentację binarną liczby, jej przybliżenia górne i dolne oraz błąd przybliżenia dla podanej liczby zmiennoprzecinkowej z określoną tolerancją.</p>

# Zajęcia nr. 2: <br>

## Funkcje

### 1. **fib()**
   - Generuje i wyświetla ciąg Fibonacciego, aż do wartości mniejszej niż 1000.

### 2. **pierwisatki()**
   - Rozwiązuje równanie kwadratowe dla podanych współczynników A, B, C.
   - Obsługuje przypadki zerowego współczynnika A, negatywnej delty i innych błędów wejściowych.

### 3. **zadanie1()**
   - Wywołuje funkcję `pierwisatki()` i wyświetla jej wyniki.
   - Obsługuje błędy związane z brakiem funkcji `pierwisatki`.

### 4. **zadanie2()**
   - Wczytuje liczby z pliku `dane.txt`, oblicza średnią, wariancję i odchylenie standardowe.
   - Obsługuje błędy braku pliku, błędnych danych i dzielenia przez zero.

### 5. **funkcja1(x)** i **funkcja2(x)**
   - Implementują specyficzne funkcje matematyczne do porównań wyników.

### 6. **zadanie3()**
   - Wykonuje obliczenia przy pomocy `funkcja1` i `funkcja2` dla różnych wartości `x`, wyświetlając wyniki.
   - Obsługuje błędy związane z brakiem definicji funkcji oraz inne niespodziewane błędy.

### 7. **re(n, x0, x1)**
   - Oblicza `n`-ty wyraz ciągu rekurencyjnego na podstawie początkowych wartości `x0` i `x1`.
   - Obsługuje błędy związane z nieprawidłowym typem danych i wartością `n`.

### 8. **zadanie4()**
   - Wykonuje obliczenia dla funkcji rekurencyjnej `re` oraz wyrażenia `np.pow(x, 20)`.
   - Obsługuje błędy definicji funkcji `re`, importu `numpy`, dzielenia przez zero i innych niespodziewanych błędów.

### 9. **wybor(argument)**
   - Wybiera i uruchamia jedną z funkcji (`zadanie1`, `zadanie2`, `zadanie3`, `zadanie4`) na podstawie przekazanego argumentu.

## Użycie

Aby uruchomić skrypt z odpowiednim zadaniem, należy podać numer zadania jako argument przy uruchamianiu skryptu z wiersza poleceń:
```bash
python nazwa_skryptu.py <numer_zadania>
```

# Zajęcia nr 3. i 4.
Interpolacja Wielomianowa i Wielomiany Czebyszewa <br>

## Funkcje i Zadania

### 1. **lagrange_interpolation_with_polynomial(x_points, y_points)**
   - Oblicza wielomian interpolacyjny Lagrange’a dla podanych punktów.
   - Używana w zadaniach do przybliżenia różnych funkcji.

### 2. **sins(x)**
   - Funkcja sinusoidalna do interpolacji w zadaniu 1.

### 3. **plot_lagrange_polynomials(polynomials, x_points_sets, y_points_sets, func, func_name=r'$sin(2\pi x)$')**
   - Generuje wykresy porównawcze interpolacji Lagrange’a dla różnych zestawów punktów.
   - Oblicza i wyświetla błąd średniokwadratowy (MSE) dla interpolacji.

## Zadania

### 1. **zad1()**
   - Interpolacja funkcji sinusoidalnej za pomocą wielomianu Lagrange’a z różnymi zestawami punktów.
   - Zapisuje wykres do pliku `fig.png`.

### 2. **zad2()**
   - Interpolacja funkcji Rungego przy użyciu punktów równomiernie rozmieszczonych.
   - Zapisuje wykres do pliku z nazwą `funkcja rungego`.

### 3. **zad3()**
   - Interpolacja funkcji "Monster Weierstrassa" (złożonej funkcji trygonometrycznej) za pomocą wielomianu Lagrange’a.

### 4. **zad4()**
   - Generowanie wykresu dla pierwszych kilku wielomianów Czebyszewa.
   - Zapisuje wynikowy wykres w `czebuszew.png`.

### 5. **zad5()**
   - Interpolacja funkcji Rungego z punktami Czebyszewa (zoptymalizowanymi punktami dla lepszego przybliżenia).
   - Generuje wykres interpolacji.

## Uruchamianie Skryptu

Skrypt pozwala na wywołanie różnych zadań przez podanie argumentu wiersza poleceń:

```bash
python nazwa_skryptu.py <numer_zadania>
```

# Zajęcia 5 i 6

Hermite i Lagrange Interpolacja

## Funkcje

### 1. **hermite(x_values, y_values, dy_values, x)**
   - Wykonuje interpolację Hermite’a dla danego zestawu punktów \( x, y \) oraz pochodnych \( dy \).
   - Tworzy macierz różnic dzielonych i oblicza wartości funkcji na podstawie wartości węzłów i ich pochodnych.

### 2. **MSE(true_val, fnc_val)**
   - Oblicza błąd średniokwadratowy (MSE) między wartościami rzeczywistymi funkcji a wartościami przybliżonymi.
   - Służy do oceny dokładności interpolacji.

### 3. **inet()**
   - Funkcja główna, która:
     - Definiuje funkcję \( f(x) = x^3 \cos(x) \) oraz jej pochodną.
     - Generuje punkty dla interpolacji Lagrange’a i Hermite’a.
     - Rysuje wykres porównawczy obu interpolacji oraz funkcji oryginalnej.
     - Oblicza i wyświetla MSE dla obu metod interpolacji.

## Wykorzystanie

Aby uruchomić skrypt i wykonać interpolację, wystarczy użyć polecenia:
```bash
python nazwa_skryptu.py
```

# Numerical Methods for Bioinformatics

# Session 1: <br>
   File: ```binary.py``` <br>
   Operations for converting decimal floating-point numbers to binary and vice versa, along with demonstrating conversion error.
   * ```float_to_binary```: Converts a floating-point number to binary format with precision specified by tolerance.
   * ```find_upper_and_lower_approximation```: Finds and returns the nearest binary approximations (upper and lower) for a given floating-point number within a specified tolerance.
   * ```binary_fraction_to_exponent```: Transforms a binary fraction into normalized scientific notation, returning the mantissa and exponent.
    <p>The script calculates and displays the binary representation of a number, its upper and lower approximations, and the approximation error for a given floating-point number with specified tolerance.</p>

# Session 2: <br>

## Functions

### 1. **fib()**
   - Generates and displays the Fibonacci sequence up to values less than 1000.

### 2. **pierwisatki()**
   - Solves a quadratic equation for given coefficients A, B, and C.
   - Handles cases of zero coefficient A, negative delta, and other input errors.

### 3. **zadanie1()**
   - Calls the `pierwisatki()` function and displays its results.
   - Handles errors related to the absence of the `pierwisatki` function.

### 4. **zadanie2()**
   - Reads numbers from the `dane.txt` file, calculates the mean, variance, and standard deviation.
   - Handles errors related to file absence, incorrect data, and division by zero.

### 5. **funkcja1(x)** and **funkcja2(x)**
   - Implement specific mathematical functions for comparison of results.

### 6. **zadanie3()**
   - Performs calculations using `funkcja1` and `funkcja2` for various `x` values, displaying the results.
   - Handles errors related to undefined functions and other unexpected errors.

### 7. **re(n, x0, x1)**
   - Calculates the `n`-th term of a recursive sequence based on initial values `x0` and `x1`.
   - Handles errors related to incorrect data types and `n` value.

### 8. **zadanie4()**
   - Performs calculations for the recursive function `re` and expression `np.pow(x, 20)`.
   - Handles errors in function definition `re`, importing `numpy`, division by zero, and other unexpected errors.

### 9. **wybor(argument)**
   - Selects and runs one of the functions (`zadanie1`, `zadanie2`, `zadanie3`, `zadanie4`) based on the provided argument.

## Usage

To run the script with a specific task, provide the task number as an argument when running the script from the command line:
```bash
python script_name.py <task_number>
```

# Sessions 3 and 4
Polynomial Interpolation and Chebyshev Polynomials <br>

## Functions and Tasks

### 1. **lagrange_interpolation_with_polynomial(x_points, y_points)**
   - Computes the Lagrange interpolation polynomial for given points.
   - Used in tasks to approximate various functions.

### 2. **sins(x)**
   - Sinusoidal function for interpolation in task 1.

### 3. **plot_lagrange_polynomials(polynomials, x_points_sets, y_points_sets, func, func_name=r'$sin(2\pi x)$')**
   - Generates comparison plots of Lagrange interpolation for different sets of points.
   - Calculates and displays the mean squared error (MSE) for interpolation.

## Tasks

### 1. **zad1()**
   - Interpolates a sinusoidal function using the Lagrange polynomial with different sets of points.
   - Saves the plot to the file `fig.png`.

### 2. **zad2()**
   - Interpolates the Runge function using evenly spaced points.
   - Saves the plot to a file named `Runge function`.

### 3. **zad3()**
   - Interpolates the "Weierstrass Monster" function (a complex trigonometric function) using the Lagrange polynomial.

### 4. **zad4()**
   - Generates a plot for the first few Chebyshev polynomials.
   - Saves the resulting plot in `chebyshev.png`.

### 5. **zad5()**
   - Interpolates the Runge function using Chebyshev points (optimized points for better approximation).
   - Generates an interpolation plot.

## Running the Script

The script allows different tasks to be called by providing a command-line argument:

```bash
python script_name.py <task_number>
```

# Sessions 5 and 6

Hermite and Lagrange Interpolation

## Functions

### 1. **hermite(x_values, y_values, dy_values, x)**
   - Performs Hermite interpolation for a given set of points \( x, y \) and derivatives \( dy \).
   - Creates a divided difference matrix and calculates function values based on node values and their derivatives.

### 2. **MSE(true_val, fnc_val)**
   - Calculates the mean squared error (MSE) between true function values and approximated values.
   - Used to evaluate interpolation accuracy.

### 3. **inet()**
   - Main function that:
     - Defines the function \( f(x) = x^3 \cos(x) \) and its derivative.
     - Generates points for Lagrange and Hermite interpolation.
     - Plots a comparison of both interpolations and the original function.
     - Calculates and displays MSE for both interpolation methods.

## Usage

To run the script and perform interpolation, simply use the command:
```bash
python script_name.py
```