# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt
import numpy as np

# Definiowanie danych na temat urodzeń w formie listy krotek (chłopcy, dziewczęta)
dane = [(100, 90), (110, 95), (120, 105), (130, 110)]

# Przekształcenie danych do odpowiednich list
chlopcy, dziewczeta = zip(*dane)

# Definiowanie etykiet dla osi X (lata)
lata = ['Rok 2020', 'Rok 2021', 'Rok 2022', 'Rok 2023']

# Definiowanie szerokości słupków
szerokosc = 0.35

# Tworzenie nowej figury (okna) o rozmiarze 10x6 cali
plt.figure(figsize=(10, 6))

# Generowanie pozycji dla słupków
indeksy = np.arange(len(lata))

# Rysowanie słupków dla chłopców
plt.bar(indeksy - szerokosc/2, chlopcy, szerokosc, label='Chłopcy', color='blue')

# Rysowanie słupków dla dziewcząt
plt.bar(indeksy + szerokosc/2, dziewczeta, szerokosc, label='Dziewczęta', color='orange')

# Dodanie etykiet osi X
plt.xlabel('Rok')

# Dodanie etykiety osi Y
plt.ylabel('Liczba urodzonych dzieci')

# Dodanie tytułu wykresu
plt.title('Liczba urodzonych dzieci według płci w danym roku')

# Dodanie etykiet dla osi X
plt.xticks(indeksy, lata)

# Dodanie legendy do wykresu
plt.legend()

# Dodanie siatki do wykresu
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
