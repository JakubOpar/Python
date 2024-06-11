# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Definiowanie danych na temat wzrostu (w cm) i masy ciała (w kg) dla grupy osób
# Przykładowe dane: [(wzrost, masa ciała), ...]
dane = [(160, 55), (165, 60), (170, 65), (175, 70), (180, 75), (185, 80), (190, 85)]

# Przekształcenie danych do odpowiednich list
wzrost, masa_ciala = zip(*dane)

# Tworzenie nowej figury (okna) o rozmiarze 10x6 cali
plt.figure(figsize=(10, 6))

# Rysowanie wykresu punktowego
plt.scatter(wzrost, masa_ciala, color='blue', label='Osoby')

# Dodanie etykiety osi X
plt.xlabel('Wzrost (cm)')

# Dodanie etykiety osi Y
plt.ylabel('Masa ciała (kg)')

# Dodanie tytułu wykresu
plt.title('Zależność masy ciała od wzrostu')

# Dodanie legendy do wykresu
plt.legend()

# Dodanie siatki do wykresu
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
