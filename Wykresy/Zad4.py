# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Importowanie biblioteki numpy do obliczeń matematycznych
import numpy as np

# Definiowanie zakresu wartości x od 0 do 2π z krokiem 0.1
x = np.arange(0, 2 * np.pi, 0.1)

# Obliczanie wartości y dla funkcji sin(x)
y_sin = np.sin(x)

# Obliczanie wartości y dla funkcji cos(x)
y_cos = np.cos(x)

# Tworzenie nowej figury (okna) o rozmiarze 8x6 cali
plt.figure(figsize=(8, 6))

# Rysowanie wykresu linii dla wartości x i y_sin
plt.plot(x, y_sin, label='sin(x)', color='blue')

# Rysowanie wykresu linii dla wartości x i y_cos
plt.plot(x, y_cos, label='cos(x)', color='red')

# Dodanie etykiety osi X
plt.xlabel("x")

# Dodanie etykiety osi Y
plt.ylabel("y")

# Dodanie tytułu wykresu
plt.title("Wykres funkcji sin(x) i cos(x)")

# Dodanie legendy do wykresu
plt.legend()

# Dodanie siatki do wykresu
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
