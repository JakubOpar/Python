print("Hello world!")

# import module_name
# from module_name import element name
# from module_name import *

print("\n__________________________LICZBY_________________________________\n")

a = 10
b = 3.5678
c = 1 + 3j

print("a = ", a)
print("b = ", b)
print("c = ", c)

print("\n___________________________ŁAŃCUCHY ZNAKÓW______________________________\n")

s = "Hello world"
print("przykładowy łańcuch znaków: ", s)

print("\n________________________________LISTY____________________________________\n")

lista = [1, 2, ['a', 'b'], 3]

print("Przykładowa lista: ", lista)

print("Pierwszy element listy:", lista[0])

print("Trzeci element listy (który jest listą):", lista[2])

print("Pierwszy element z trzeciego elementu listy:", lista[2][0])

print("len(lista) = ", len(lista))

print("\n________________________________SŁOWNIKI_____________________________________\n")

slownik = {'imie': 'Jan', 'nazwisko': 'Kowalski'}

print("Slownik: ", slownik)

print("Wartość skojarzona z kluczem 'imie':", slownik['imie'])

print("Wartość skojarzona z kluczem 'nazwisko':", slownik['nazwisko'])

print("\n__________________________OPERATORY ARYTMETYCZNE________________________________\n")

x = 5
y = 3
z = 2
ux = -7

print("Konwersja na typ całkowity: int(5.7) = ", int(5.7))
print("Konwersja na typ całkowity nieskończony: long(5) = ",
      int(5))  # W Pythonie 3 `long` nie istnieje, `int` obsługuje duże liczby
print("Konwersja na typ zmiennoprzecinkowy: float(5) = ", float(5))
print("Liczba zespolona: complex(5, 3) = ", complex(5, 3))
print("Para (iloraz, reszta) z divmod: divmod(5, 3) = ", divmod(5, 3))
print("Potęga za pomocą pow: pow(5, 3) = ", pow(5, 3))
print("Potęga za pomocą operatora **: 5 ** 3 = ", 5 ** 3)

print("\nOperacje arytmetyczne:")
print("Dodawanie: ", x, " + ", y, " = ", (x + y))
print("Odejmowanie: ", x, " - ", y, " = ", (x - y))
print("Iloczyn: ", x, " * ", y, " = ", (x * y))
print("Iloraz: ", x, " / ", z, " = ", (x / z))
print("Zaokrąglony w dół iloraz: ", x, " // ", z, " = ", (x // z))
print("Reszta z dzielenia: ", x, " % ", z, " = ", (x % z))
print("Liczba ujemna: -", x, " = ", -x)
print("Liczba dodatnia: +", x, " = ", +x)
print("Wartość bezwzględna: |", ux, "| = ", abs(ux))

print("\n____________________________ŁAŃCUCHY TEKSTOWE____________________________________\n")

sA = """Witaj świecie sA!"""
sB = "Witaj ponownie sB"
sC = 'Witaj ponownie sC'

print("sA = ", sA)
print("sB = ", sB)
print("sC = ", sC)

print("sA[2] = ", sA[2])
print("sA[4:7] = ", sA[1:7])
print("sA[-1] = ", sA[-1])

print("sA[0] = a")
print("TypeError: 'str' object does not support item assignment")

print("sA + 'kontynuacja' = ", sA + 'kontynuacja')

print("\n____________________________________KROTKI__________________________________________\n")

T = (1, 'x', 3)

print("T = ", T)

T2 = T + (3,'x')

print("T + (3, 'x') = ", T2)

print("\n______________________________INSTRUKCJE WARUNKOWE____________________________________\n")

temperature = 25

if temperature > 30:
    print("Jest gorąco! Pamiętaj o nawadnianiu się.")
elif temperature > 20:
    print("Jest ciepło. Można wyjść na spacer.")
elif temperature > 10:
    print("Jest chłodno. Warto założyć lekką kurtkę.")
elif temperature > 0:
    print("Jest zimno. Ubierz się ciepło.")
else:
    print("Jest bardzo zimno! Lepiej zostać w domu.")


print("\n__________________________________PĘTLA WHILE___________________________________________\n")

number = 1

while number <= 10:
    print("Liczba:", number)
    number += 1

print("\n__________________________________PĘTLA FOR___________________________________________\n")

fruits = ["jabłko", "banan", "wiśnia", "gruszka"]

for fruit in fruits:
    print("Owoc:", fruit)
