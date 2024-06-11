# Import biblioteki do tworzenia wykresów
import matplotlib.pyplot as plt

# Import biblioteki do manipulacji tablicami i macierzami
import numpy as np

# Import biblioteki do wykonywania zapytań HTTP
import requests

# klucz API OpenWeatherMap
api_key = "7a44285f2b6c4bee04cb011236bcb5a0"

# Utwórz listę współrzędnych geograficznych miast w Europie
coordinates = [
    (51.509865, -0.118092),  # Londyn
    (48.856613, 2.352222),  # Paryż
    (52.520008, 13.404954),  # Berlin
    (40.416775, -3.703790),  # Madryt
    (41.902782, 12.496366),  # Rzym
    (37.983810, 23.727539),  # Ateny
    (52.367573, 4.904138)  # Amsterdam
]

towns = ['Londyn', 'Paryż', 'Berlin', 'Madryt', 'Rzym', 'Ateny', 'Amsterdam']

# Pobierz dane temperatury dla każdego z miast

# Lista na przechowywanie temperatur
temperatures = []

for latitude, longitude in coordinates:
    # Zapytanie do API OpenWeatherMap
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(latitude, longitude,
                                                                                                    api_key))

    # Konwersja odpowiedzi na obiekt JSON
    data = response.json()

    # Sprawdzenie, czy dane dotyczące temperatury są dostępne
    if 'main' in data:

        # Pobranie temperatury
        temperature = data['main']['temp']

        # Dodanie temperatury do listy
        temperatures.append(temperature)
    else:

        # Komunikat o niepowodzeniu pobrania danych
        print("Nie udało się pobrać danych dla współrzędnych: ({}, {})".format(latitude,
                                                                               longitude))

# Stwórz tablicę numpy z danymi temperatury

# Konwersja listy temperatur na tablicę numpy
temperatures = np.array(temperatures)

# Stwórz mapę cieplną z danymi temperatury

# Dostosowanie kształtu tablicy do wymagań funkcji imshow
temperatures = temperatures.reshape(-1, 1)

# Tworzenie mapy cieplnej
plt.imshow(temperatures, cmap='coolwarm', aspect='auto')

# Dodanie podpisu kolorowej skali temperatury
plt.colorbar(label='Temperatura (°C)')

# Definicja podpisów osi

# Wyłączenie oś X
plt.xticks([])

# Ustawienie etykiet osi Y z nazwami miast
plt.yticks(np.arange(len(towns)), towns)

# Pokaż wykres
plt.show()
