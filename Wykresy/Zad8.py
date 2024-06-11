# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Definiowanie danych na temat różnych gatunków owoców w koszu
# Przykładowe dane: [(nazwa owocu, ilość), ...]
data = [('jabłka', 30), ('gruszki', 20), ('śliwki', 15), ('banany', 25), ('cytryny', 10)]

# Przekształcenie danych do odpowiednich list
owoce, ilosci = zip(*data)

# Tworzenie nowej figury (okna) o rozmiarze 8x8 cali
plt.figure(figsize=(8, 8))

# Rysowanie wykresu kołowego
plt.pie(ilosci, labels=owoce, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'purple', 'yellow', 'gold'])

# Dodanie tytułu wykresu
plt.title('Rozkład procentowy różnych gatunków owoców w koszu')

# Wyświetlenie wykresu
plt.show()
