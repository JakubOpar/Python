# Importuje bibliotekę numpy i nadaje jej alias np
import numpy as np

# Importuje moduł pyplot z biblioteki matplotlib i nadaje mu alias plt
import matplotlib.pyplot as plt

# Definiuje funkcję sine, która przyjmuje argument x
def sine(x):
    # Oblicza wartość bezwzględną x i przypisuje ją do zmiennej x_abs
    x_abs = np.abs(x)

    # Zwraca wartość funkcji sinus z zastosowaniem określonej formuły
    return np.power(x_abs, (2.0 / 3)) + 0.9 * (3.3 - x_abs ** 2) ** (1 / 2) * np.sin(10 * np.pi * x_abs)

# Tworzy 100 równoodległych punktów między -2 a 2 i przypisuje je do zmiennej x_values
x_values = np.linspace(-2, 2, 100)

# Wywołuje funkcję sine dla każdego punktu x_values i przypisuje wyniki do zmiennej y_values
y_values = sine(x_values)

# Tworzy wykres na podstawie wartości x_values i y_values, ustawiając kolor linii na czerwony
plt.plot(x_values, y_values, color='red')

# Dodaje opis osi x jako 'x'
plt.xlabel('x')

# Dodaje opis osi y jako 'sine(x)'
plt.ylabel('sine(x)')

# Dodaje tytuł wykresu jako 'Wykres funkcji sine(x)'
plt.title('Wykres funkcji sine(x)')

# Włącza siatkę na wykresie
plt.grid(True)

# Ustawia zakres osi x od -4 do 4
plt.xlim(-4, 4)

# Ustawia zakres osi y od -3 do 3
plt.ylim(-3, 3)

# Wyświetla wykres
plt.show()
