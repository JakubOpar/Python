# Przykłady obsługi wyjątków

print("\n__________________________OBSŁUGA WYJĄTKÓW_________________________________\n")

# Błędy składniowe są wykrywane na etapie parsowania pliku przez interpreter
# Wyjątkami nazywamy błędy, które wystąpiły w trakcie uruchomienia skryptu

# Przykłady błędów
try:
    10 * (1/0)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

try:
    4 + a * 3
except NameError as e:
    print(f"NameError: {e}")

# Przykłady wyjątków
print("Exception - podstawowa klasa dla wyjątków.")
print("NameError - gdy w przestrzeniach nazw (lokalnych lub globalnej) nie znaleziono nazwy.")
print("IOError - gdy występuje błąd operacji wejścia/wyjścia.")
print("ImportError - gdy nie można odnaleźć importowanego pakietu.")
print("IndexError - gdy indeks sekwencji jest poza zakresem.")
print("KeyError - gdy nie można odnaleźć danego klucza w słowniku.")

# Błędy składniowe
try:
    exec("while 1 print('Cześć świecie')")
except SyntaxError as e:
    print(f"SyntaxError: {e}")

# Klauzula try-except
try:
    f = open('1.tx')
except Exception:
    print('Plik nie istnieje!')

# Klauzula try-except z konkretnymi wyjątkami
try:
    f = open('1.tx')
except FileNotFoundError:
    print('Plik nie istnieje!')
except Exception as e:
    print('Błąd! Coś poszło nie tak.')
    print(e)

# Klauzula try-except-else
try:
    f = open('1.tx')
except FileNotFoundError:
    print('Plik nie istnieje!')
else:
    print(f.read())
    f.close()

# Klauzula try-except-else-finally
try:
    f = open('1.tx')
except FileNotFoundError:
    print('Plik nie istnieje!')
else:
    print(f.read())
    f.close()
finally:
    print("Ostatecznie (...)")

# Czy można za pomocą klauzuli try-except przechwytywać błędy składniowe?
print("Czy można za pomocą klauzuli try-except przechwytywać błędy składniowe?")
print("Tylko przy wywołaniach funkcji eval lub exec")

# Przykład użycia eval
x = 1
print(eval('x + 1'))  # 2

# Obsługa plików

print("\n__________________________OBSŁUGA PLIKÓW_________________________________\n")

# Składnia otwierania pliku
file = open('test.txt', 'w')
file.write("To jest testowy plik.")
file.close()

# Tryby dostępu do pliku
print("r - Otwiera plik tylko do odczytu. Wskaźnik pliku jest umieszczony na początku pliku. Jest to domyślny tryb.")
print("rb - Otwiera plik tylko do odczytu w formacie binarnym. Wskaźnik pliku jest umieszczony na początku pliku.")
print("r+ - Otwiera plik do odczytu i zapisu. Wskaźnik pliku jest umieszczony na początku pliku.")
print("rb+ - Otwiera plik do odczytu i zapisu w formacie binarnym. Wskaźnik pliku jest umieszczony na początku pliku.")
print("w - Otwiera plik tylko do zapisu. Nadpisuje plik, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu.")
print("wb - Otwiera plik tylko do zapisu w formacie binarnym. Nadpisuje plik, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu.")
print("w+ - Otwiera plik do zapisu i odczytu. Nadpisuje istniejący plik, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu i odczytu.")
print("wb+ - Otwiera plik do zapisu i odczytu w formacie binarnym. Nadpisuje istniejący plik, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu i odczytu.")
print("a - Otwiera plik do dopisywania. Wskaźnik pliku jest na końcu pliku, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu.")
print("ab - Otwiera plik do dopisywania w formacie binarnym. Wskaźnik pliku jest na końcu pliku, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu.")
print("a+ - Otwiera plik do dopisywania i odczytu. Wskaźnik pliku jest na końcu pliku, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu i odczytu.")
print("ab+ - Otwiera plik do dopisywania i odczytu w formacie binarnym. Wskaźnik pliku jest na końcu pliku, jeśli plik istnieje. Jeśli plik nie istnieje, tworzy nowy plik do zapisu i odczytu.")

print("\n__________________________PAMIĘTAMY O ZAMYKANIU PLIKÓW!_________________________________\n")

# Pamiętamy o zamykaniu plików!
file = open('test.txt', 'r')
print(file.read())
file.close()

print("\n__________________________CO SIĘ STANIE, JEŚLI PLIKU NIE ZAMKNIEMY?_________________________________\n")

# Co się stanie, jeśli pliku nie zamkniemy?
# try:
#    files = []
#    for x in range(100000):
# files.append(open('test.txt', 'w'))
# except OSError as e:
#    print(f"OSError: {e}")

# Traceback (most recent call last):
# OSError: [Errno 24] Too many open files: 'test.txt'

print("\n__________________________UŻYWANIE PLIKU - CONTEXT MANAGERS_________________________________\n")

# Używanie pliku - context managers
with open('test.txt', 'r') as f:
    print(f.read())

print(f.closed)  # True

print("\n__________________________UŻYWANIE PLIKU - CZYTANIE ZAWARTOŚCI_________________________________\n")

# Używanie pliku - czytanie zawartości
with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('test.txt', 'r') as f:
    for line in f:
        print(line.strip())

print("\n__________________________UŻYWANIE PLIKU - ZAPIS I DOPISYWANIE_________________________________\n")

# Używanie pliku
with open('test.txt', 'w') as f:
    f.write("Dodajemy trochę tekstu.\n")

with open('test.txt', 'r') as f:
    print(f.read())

with open('test.txt', 'a') as f:
    f.write("Dopisujemy więcej tekstu.\n")

with open('test.txt', 'r') as f:
    print(f.read())

print("\n__________________________METODY PLIKU_________________________________\n")

# Metody pliku
with open('test.txt', 'r') as f:
    print(f.read(10))  # Czyta pierwsze 10 bajtów
    print(f.tell())  # Zwraca aktualną pozycję w pliku
    f.seek(0)  # Ustawia wskaźnik pliku na początek
    print(f.read(10))  # Czyta pierwsze 10 bajtów ponownie

print("\n__________________________BIBLIOTEKA STANDARDOWA - MODUŁ OS_________________________________\n")

# Biblioteka standardowa - moduł os
import os

# Przykładowe użycie funkcji z modułu os
print(os.getcwd())  # Zwraca bieżący katalog roboczy
os.mkdir('nowy_katalog')  # Tworzy nowy katalog
os.rmdir('nowy_katalog')  # Usuwa katalog
files = os.listdir('.')  # Zwraca listę plików w bieżącym katalogu
print(files)


print("\n__________________________MODUŁ OS_________________________________\n")

import os

# Pobranie bieżącego katalogu
print(os.getcwd())

# Zmiana bieżącego katalogu
os.mkdir('nowy_katalog')
os.chdir('nowy_katalog')
print(os.getcwd())

# Tworzenie i usuwanie folderów
os.chdir('..')
os.rmdir('nowy_katalog')
print(os.path.exists('nowy_katalog'))  # False

# Biblioteka standardowa - moduł socket

print("\n__________________________MODUŁ SOCKET_________________________________\n")

import socket

# Klient
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.connect(("www.python.org", 80))
print("Połączenie z serwerem na porcie 80 nawiązane.")

# Serwer
servsockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsockt.bind((socket.gethostname(), 12345))
servsockt.listen(5)
print("Serwer nasłuchuje na porcie 12345.")
