# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Importowanie biblioteki numpy do obliczeń matematycznych
import numpy as np

# Definiowanie zakresu wartości x i y od -2 do 2 z krokiem 0.1
x = np.arange(-2, 2.1, 0.1)
y = np.arange(-2, 2.1, 0.1)

# Tworzenie siatki punktów (x, y)
x, y = np.meshgrid(x, y)

# Obliczanie wartości z dla każdego punktu siatki, gdzie z = x^2 + y^2
z = x**2 + y**2

# Tworzenie nowej figury (okna) o rozmiarze 10x8 cali
fig = plt.figure(figsize=(10, 8))

# Dodanie subplotu 3D do figury
ax = fig.add_subplot(111, projection='3d')

# Rysowanie powierzchni 3D
surface = ax.plot_surface(x, y, z, cmap='viridis')

# Dodanie paska kolorów (color bar) do figury
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# Dodanie etykiety osi X
ax.set_xlabel("x")

# Dodanie etykiety osi Y
ax.set_ylabel("y")

# Dodanie etykiety osi Z
ax.set_ylabel("z")

# Dodanie tytułu wykresu
ax.set_title("Wykres 3D powierzchni z = x^2 + y^2")

# Wyświetlenie wykresu
plt.show()
