# Przykłady funkcji

print("\n__________________________FUNKCJE_________________________________\n")

# Przykład podstawowej funkcji
def sub(a, b):
    return a - b

print(sub(2, 1))  # 1

# Funkcja z użyciem keyword arguments
print(sub(a=2, b=1))  # 1

# Funkcja przyjmująca wiele argumentów
def many(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

many(1, 2, 3, a=4, b=5)

# Moduły i pakiety

print("\n__________________________MODUŁY I PAKIETY_________________________________\n")

# Importowanie modułów i ich elementów
from decimal import Decimal
from fractions import Fraction

print(Decimal('10.5'))  # 10.5
print(Fraction(22, 7))  # 22/7

# Ścieżka wyszukiwania modułów
import sys
print("Ścieżka wyszukiwania modułów:", sys.path)

# Przykład struktury pakietów
# Zakładając strukturę katalogów:
# dir1/
# └── dir2/
#     └── mod.py

# import dir1.dir2.mod
# Kod w mod.py:
# def hello():
#     return "Hello from mod.py"

# print(dir1.dir2.mod.hello())  # Hello from mod.py

# Definiowanie klas

print("\n__________________________KLASY_________________________________\n")

# Najprostsza definicja klasy
class Pracownik:
    pass

janek = Pracownik()  # Tworzy pusty rekord pracownika

# Wypełnienie pól w rekordzie
janek.nazwa = 'Jan Kowalski'
janek.miejsce = 'laboratorium komputerowe'
janek.pensja = 4000

print(janek.nazwa, janek.miejsce, janek.pensja)

# Zmienna klasy vs zmienna obiektu
class Connection:
    verbose = 0

    def debug(self):
        self.verbose = 1

c = Connection()
c.debug()
print(c.verbose)  # 1

c = Connection()
print(c.verbose)  # 0

# Metody __init__() i __del__()
class Example:
    def __init__(self, value):
        self.value = value
        print(f"Tworzenie instancji z wartością {value}")

    def __del__(self):
        print(f"Usuwanie instancji z wartością {self.value}")

ex = Example(10)
del ex  # Usuwanie instancji

# Przeciążanie metod (nie działa w Pythonie)
class C:
    def meth(self, x):
        print("meth z jednym argumentem")

    def meth(self, x, y, z):
        print("meth z trzema argumentami")

# Tylko druga definicja metody jest widoczna
c = C()
# c.meth(1)  # Błąd: meth() missing 2 required positional arguments: 'y' and 'z'
c.meth(1, 2, 3)  # meth z trzema argumentami
