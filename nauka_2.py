print("\n__________________________METODY LISTY_________________________________\n")

# Początkowa lista
lista = [1, 2, 3, 4, 3, 6]
print("Początkowa lista:\n", lista, "\n")

# Dodanie 'a' na końcu listy za pomocą append()
lista.append('a')
print("Po dodaniu 'a' na końcu listy za pomocą append():\n", lista, "\n")

# Rozszerzenie listy o elementy z lista2 za pomocą extend()
lista2 = ['a', 'b']
lista.extend(lista2)
print("Po rozszerzeniu listy o elementy z lista2 za pomocą extend():\n", lista, "\n")

# Liczba wystąpień 'a' w liście za pomocą count()
print("Liczba wystąpień 'a' w liście za pomocą count():\n lista.count('a') =", lista.count('a'), "\n")

# Indeks pierwszego wystąpienia 3 w liście za pomocą index()
print("Indeks pierwszego wystąpienia 3 w liście za pomocą index():\n lista.index(3) =", lista.index(3), "\n")

# Usunięcie ostatniego elementu z listy za pomocą pop()
print("Ostatni element usunięty z listy za pomocą pop():\n lista.pop() =", lista.pop(), "\n")
print("Lista po usunięciu ostatniego elementu za pomocą pop():\n", lista, "\n")

# Usunięcie pierwszego wystąpienia 2 z listy za pomocą remove()
lista.remove(2)
print("Lista po usunięciu pierwszego wystąpienia 2 za pomocą remove():\n", lista, "\n")

# Odwrócenie kolejności elementów w liście za pomocą reverse()
lista.reverse()
print("Lista po odwróceniu kolejności elementów za pomocą reverse():\n", lista, "\n")

# Sortowanie listy2 w porządku rosnącym za pomocą sort()
lista2 = [10, 2, 3, 4, 3, 6]
lista2.sort()
print("Lista2 po posortowaniu w porządku rosnącym za pomocą sort():\n", lista2, "\n")

print("\n__________________________KONWERSJE_________________________________\n")

# Konwersja krotki na listę i zbiór
t = (1, 2, 3)
print("Początkowa krotka:", t)

lista_z_krotki = list(t)
print("Lista na podstawie krotki:", lista_z_krotki)

zbior_z_krotki = set(t)
print("Zbiór na podstawie krotki:", zbior_z_krotki)

print("\n")

# Konwersja listy na krotkę
l = [1, 2, 3]
print("Początkowa lista:", l)

krotka_z_listy = tuple(l)
print("Krotka na podstawie listy:", krotka_z_listy)

print("\n")

# Konwersja zbioru na listę i krotkę
s = {1, 2, 3}
print("Początkowy zbiór:", s)

lista_z_zbioru = list(s)
print("Lista na podstawie zbioru:", lista_z_zbioru)

krotka_z_zbioru = tuple(s)
print("Krotka na podstawie zbioru:", krotka_z_zbioru)

zbior_z_listy = set(l)
print("Zbiór na podstawie listy:", zbior_z_listy)

print("\n__________________________RANGE_________________________________\n")

# Iteracja przez zakres
print("Iteracja przez zakres:")
for i in range(5):
    print(i)

print("\n")

# Generowanie sekwencji liczb od 1 do 10 z krokiem 2
seq = range(1, 11, 2)
print("Generowanie sekwencji liczb od 1 do 10 z krokiem 2:", list(seq))

print("\n")

# Generowanie sekwencji liczb od 10 do 1 z krokiem -1
seq2 = range(10, 0, -1)
print("Generowanie sekwencji liczb od 10 do 1 z krokiem -1:", list(seq2))

print("\n__________________________LIST COMPREHESIONS_________________________________\n")

# Generowanie listy kwadratów liczb od 0 do 9, pomnożonych przez 2, tylko dla liczb parzystych
squares = [x ** 2 * 2 for x in range(10) if x % 2 == 0]
print("Lista kwadratów liczb od 0 do 9, pomnożonych przez 2, tylko dla liczb parzystych:", squares)

print("\n__________________________SŁOWNIKI_________________________________\n")

# Tworzenie i operacje na słowniku
d = {'name': 'Jack', 'age': 26}

print("Imię:", d['name'])
print("Wiek:", d['age'])

d['city'] = 'London'
print("Słownik po dodaniu elementu:", d)

del d['city']
print("Słownik po usunięciu elementu:", d)

# Słowniki zagnieżdżone
rec = {'personal_data': {'first_name': 'John', 'last_name': 'Doe'}, 'age': 35}

print("Nazwisko:", rec['personal_data']['last_name'])
print("Wiek:", rec['age'])

rec2 = {'occupation': ['engineer', 'designer']}

rec2['occupation'].append('mechanic')
print("Lista zawodów po dodaniu:", rec2['occupation'])

print("\n__________________________REFERENCJE_________________________________\n")

# Przykład referencji
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print("\n__________________________FUNKCJE_________________________________\n")


def pole_prostokata(a, b):
    """Funkcja oblicza pole prostokąta."""
    return a * b


# Przykładowe użycie funkcji pole_prostokata
szerokosc = 4
dlugosc = 6
print("Pole prostokąta:", pole_prostokata(szerokosc, dlugosc))


def dodaj(*args):
    """Funkcja dodaje dowolną liczbę argumentów."""
    suma = 0
    for arg in args:
        suma += arg
    return suma


# Przykładowe użycie funkcji dodaj
print("Suma liczb:", dodaj(1, 2, 3, 4, 5))
