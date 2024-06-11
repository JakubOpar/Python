# Importowanie biblioteki matplotlib.pyplot do tworzenia wykresów
import matplotlib.pyplot as plt

# Przykładowe dane temperatur dla tygodnia (poniedziałek - niedziela)
temperatury = [20, 22, 19, 23, 25, 21, 24]

# Nazwy dni tygodnia odpowiadające powyższym temperaturom
dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

# Tworzenie nowej figury (okna) o rozmiarze 10x5 cali
plt.figure(figsize=(10, 5))

# Tworzenie wykresu słupkowego z danymi temperatur i dni tygodnia
plt.bar(dni_tygodnia, temperatury, color='skyblue')

# Dodanie etykiety osi X
plt.xlabel("Dzień tygodnia")

# Dodanie etykiety osi Y
plt.ylabel("Temperatura (°C)")

# Dodanie tytułu wykresu
plt.title("Temperatury w poszczególnych dniach tygodnia")

# Obrócenie etykiet osi X o 45 stopni dla lepszej czytelności
plt.xticks(rotation=45)

# Dodanie siatki poziomej do wykresu
plt.grid(axis='y', linestyle='--', linewidth=0.7)

# Dostosowanie układu wykresu do zawartości
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()
