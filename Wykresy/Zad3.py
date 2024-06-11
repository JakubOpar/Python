# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Importowanie biblioteki numpy do obliczeń matematycznych
import numpy as np

# Definiowanie zakresu wartości x od -5 do 5 z krokiem 0.1
x = np.arange(-5, 5.1, 0.1)

# Obliczanie wartości y dla każdego x, gdzie y = x^2
y = x**2

# Tworzenie nowej figury (okna) o rozmiarze 8x6 cali
plt.figure(figsize=(8, 6))

# Rysowanie wykresu linii dla wartości x i y
plt.plot(x, y, label='y = x^2', color='blue')

# Dodanie etykiety osi X
plt.xlabel("x")

# Dodanie etykiety osi Y
plt.ylabel("y")

# Dodanie tytułu wykresu
plt.title("Wykres funkcji y = x^2")

# Dodanie legendy do wykresu
plt.legend()

# Dodanie siatki do wykresu
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
