# Importowanie biblioteki matplotlib.pyplot, która będzie używana do rysowania histogramu.
import matplotlib.pyplot as plt

# Dane dotyczące wyników testu przypisane do listy.
dane = [60, 70, 80, 90, 100, 70, 80, 80, 85, 95]

# Rysowanie histogramu na podstawie danych. Ustawienie liczby słupków (bins) na 10 i koloru krawędzi na czarny.
plt.hist(dane, bins=10, edgecolor='black')

# Dodanie opisu osi x.
plt.xlabel('Wynik')

# Dodanie opisu osi y.
plt.ylabel('Liczba studentów')

# Dodanie tytułu histogramu.
plt.title('Histogram wyników testu')

# Wyświetlenie histogramu.
plt.show()
