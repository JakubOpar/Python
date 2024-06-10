print("\n__________________________MODUŁ SOCKET_________________________________\n")

# Biblioteka standardowa - moduł socket
import socket

print("\n__________________________MODUŁ SOCKET - KLIENT_________________________________\n")

# Klient
print("Utworzenie gniazda INET")
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Połączenie z serwerem na porcie 80")
sockt.connect(("www.python.org", 80))

print("\n__________________________MODUŁ SOCKET - SERWER_________________________________\n")

# Serwer
print("Utworzenie gniazda INET")
servsockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Dowiązanie gniazda do określonego portu")
servsockt.bind((socket.gethostname(), 80))
print("Nasłuchiwanie przychodzących połączeń")
servsockt.listen(5)

print("\n__________________________MODUŁ SOCKET - SCHEMAT KOMUNIKACJI_________________________________\n")

# Moduł socket - schemat typowej komunikacji
print("client                        server")
print("                                 socket")
print("                                   |")
print("                                  bind")
print("                                   |")
print("                                 listen")
print("                                   |")
print("   socket                        accept")
print("     |                              |")
print("  connect ------------------------->|")
print("     |                              |")
print(" -->send ------------------------->recv<--")
print("|    |                              |     |")
print(" --recv<-------------------------- send --")
print("     |                              |")
print("   close ------------------------->recv")
print("                                   |")
print("                                  close")

print("\n__________________________WIRTUALNE ŚRODOWISKA_________________________________\n")

# Wirtualne środowiska

print("\n__________________________WIRTUALNE ŚRODOWISKA - MOTYWACJA_________________________________\n")

# Wirtualne środowiska - motywacja
print("W przypadkach gdy:")
print("* potrzebujemy używać różnych wersji tych samych pakietów, lub gdy pakiety mają różne zależności;")
print("* legacy code;")
print("* uruchamianie programów w tzw. sandbox-ie.")

print("\n__________________________WIRTUALNE ŚRODOWISKA - CO MAMY DO WYBORU_________________________________\n")

# Co mamy do wyboru?
print("Conda")
print("virtualenv")

print("\n__________________________CONDA_________________________________\n")

# Czym conda jest a czym nie?
print("* nie jest dystrybucją pythona (ale Anaconda już tak);")
print("* nie jest tylko i wyłącznie managerem pakietów (jak pip);")
print("* zawiera własny menadżer środowisk wirtualnych (envs);")

print("\n__________________________PIP_________________________________\n")

# pip
print("pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.")

print("\n__________________________PIP - INSTALL_________________________________\n")

print("pip install SomePackage")
print("[...]")
print("Successfully installed SomePackage")

print("\n__________________________PIP - REQUIREMENTS FILES_________________________________\n")

# pip - requirements files
print("Wygodny sposób umieszczenia listy wszystkich zależności w jednym pliku.")

print("pip install -r requirements.txt")

print("\n__________________________CONDA - INSTALACJA_________________________________\n")

# conda - instalacja

# silent mode installation
print("wget https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh")
print("bash ~/miniconda.sh -b -p $HOME/miniconda")
print("export PATH=\"$HOME/miniconda/bin:$PATH\"")

print("\n__________________________CONDA - PODSTAWOWE POLECENIA_________________________________\n")

# conda - podstawowe polecenia
print("conda create --name py35 python=3.5")
print("conda env list")
print("conda list")

print("\n__________________________CONDA - ŚCIĄGA_________________________________\n")

# conda - ściąga
print("http://tiny.cc/CondaCheats")

print("\n__________________________NUMPY_________________________________\n")

# NumPy
print("NumPy jest pakietem Pythona do obliczeń naukowych. Posiada m. in.:")
print("* wydajną implementację obiektu tablic n-wymiarowych,")
print("* mechanizmy broadcasting ułatwiające pracę z macierzami,")
print("* narzędzia do integracji kodu w językach C/C++/Fortran,")
print("* implementacje funkcji przydatnych w zagadnieniach algebry liniowej, transformat Fouriera, liczb pseudolosowych (i wielu innych).")
print("Licencja: BSD")

print("\n__________________________NUMPY - TYP DANYCH NDARRAY_________________________________\n")

# Podstawy: typ danych ndarray
print("Trzonem funkcjonalności NumPy jest obiekt n-wymiarowej tablicy ndarray. Obiekt ten przechowuje dane tego samego typu w wielowymiarowej strukturze i zapewnia szybkie operacje na tych danych (dzięki prekompilowanemu natywnemu kodowi źródłowemu).")

print("\n__________________________NDARRAY A SEKWENCJE PYTHONA_________________________________\n")

# ndarray a sekwencje Pythona (różnice)
print("Rozmiar tablic NumPy jest definiowany w momencie utworzenia obiektu i nie może zmieniać się dynamicznie (jak w przypadku list znanych z Pythona). Zmiana rozmiaru będzie skutkowała utworzeniem nowego obiektu ndarray i usunięciem dotychczasowego.")
print("Elementy tablicy muszą być tego samego typu - każdy element tablicy ma dzięki temu identyczny rozmiar w pamięci.")
print("Obiekty ndarray dostarczają za to zaawansowanych operacji matematycznych (i nie tylko), które mogą być wydajnie wykonywane na dużych ilościach danych. Pozwala to na pisanie programów szybszych w działaniu i krótszych pod względem liczby linii kodu źródłowego.")

print("\n__________________________NDARRAY - TYPY DANYCH_________________________________\n")

# Typy danych
import numpy as np

print(np.sctypeDict.keys())  # Zwraca słownik typów danych NumPy
print(np.int32)  # Typ danych int32
print(np.float64)  # Typ danych float64

print("\n__________________________NDARRAY - TWORZENIE TABLIC_________________________________\n")

# Tworzenie tablic
a = np.array([1, 2, 3])  # Tworzenie tablicy z listy
b = np.arange(10)  # Tworzenie tablicy od 0 do 9
c = np.zeros((3, 3))  # Tworzenie tablicy 3x3 wypełnionej zerami
d = np.ones((3, 3))  # Tworzenie tablicy 3x3 wypełnionej jedynkami

print("\n__________________________NDARRAY - TWORZENIE MACIERZY LOSOWYCH_________________________________\n")

# Tworzenie macierzy losowych
e = np.random.rand(3, 3)  # Macierz 3x3 z losowymi wartościami z przedziału [0, 1)
f = np.random.randn(3, 3)  # Macierz 3x3 z losowymi wartościami z rozkładu normalnego

print("\n__________________________NDARRAY - TWORZENIE TABLIC O ZADANYCH PARAMETRACH_________________________________\n")

# Tworzenie tablic o zadanych parametrach
g = np.linspace(0, 10, 5)  # Pięć liczb liniowo rozłożonych w przedziale [0, 10]
h = np.eye(4)  # Macierz jednostkowa 4x4

print("\n__________________________NDARRAY - OPIS TABLIC_________________________________\n")

# Opis tablic
print(a.ndim)  # Liczba wymiarów
print(a.shape)  # Rozmiar tablicy w każdym z wymiarów
print(a.size)  # Liczba elementów tablicy
print(a.dtype)  # Typ danych elementów
print(a.itemsize)  # Rozmiar pojedynczego elementu w bajtach
print(a.nbytes)  # Rozmiar tablicy w bajtach

print("\n__________________________NDARRAY - PODSTAWOWE OPERACJE_________________________________\n")

# Podstawowe operacje
i = np.array([1, 2, 3])
j = np.array([4, 5, 6])

print(i + j)  # Dodawanie
print(i - j)  # Odejmowanie
print(i * j)  # Mnożenie
print(i / j)  # Dzielenie
print(i ** 2)  # Potęgowanie
print(np.dot(i, j))  # Iloczyn skalarny
print(np.cross(i, j))  # Iloczyn wektorowy

print("\n__________________________NDARRAY - METODY_________________________________\n")

# Metody
k = np.array([[1, 2, 3], [4, 5, 6]])
print(k.T)  # Transpozycja
print(k.mean())  # Średnia arytmetyczna
print(k.sum())  # Suma elementów
print(k.min())  # Minimalna wartość
print(k.max())  # Maksymalna wartość

print("\n__________________________BIBLIOTEKA PANDAS_________________________________\n")

# Pandas
print("Pandas to otwartoźródłowa biblioteka do analizy danych w Pythonie, oferująca strukturę danych DataFrame do pracy z danymi tabelarycznymi, podobnie jak tabele w bazach danych lub arkusze kalkulacyjne.")
print("Licencja: BSD")

print("\n__________________________PANDAS - TYP DANYCH DATAFRAME_________________________________\n")

# DataFrame
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("\n__________________________PANDAS - PODSTAWOWE OPERACJE_________________________________\n")

# Podstawowe operacje
print(df.head())  # Pierwsze 5 wierszy
print(df.tail())  # Ostatnie 5 wierszy
print(df.describe())  # Statystyki opisowe
print(df.info())  # Informacje o DataFrame
print(df.shape)  # Kształt DataFrame (liczba wierszy i kolumn)
print(df.columns)  # Nazwy kolumn
print(df.index)  # Indeksy wierszy

print("\n__________________________PANDAS - WYSZUKIWANIE I WYBIERANIE DANYCH_________________________________\n")

# Wyszukiwanie i wybieranie danych
print(df['A'])  # Wybieranie kolumny
print(df[['A', 'B']])  # Wybieranie wielu kolumn
print(df.iloc[0])  # Wybieranie wiersza według indeksu
print(df.iloc[0:2])  # Wybieranie wielu wierszy według indeksu
print(df.loc[0, 'A'])  # Wybieranie pojedynczej wartości

print("\n__________________________PANDAS - FILTROWANIE DANYCH_________________________________\n")

# Filtrowanie danych
print(df[df['A'] > 1])  # Wiersze, gdzie wartość w kolumnie 'A' jest większa niż 1
print(df[(df['A'] > 1) & (df['B'] < 6)])  # Wiersze spełniające wiele warunków

print("\n__________________________PANDAS - OPERACJE NA KOLUMNACH_________________________________\n")

# Operacje na kolumnach
df['D'] = df['A'] + df['B']  # Dodawanie nowej kolumny
print(df)
df['E'] = df['C'] - df['B']  # Dodawanie nowej kolumny
print(df)
df['F'] = df['A'] * 2  # Dodawanie nowej kolumny
print(df)

print("\n__________________________PANDAS - AGREGACJA DANYCH_________________________________\n")

# Agregacja danych
print(df.mean())  # Średnia arytmetyczna
print(df.sum())  # Suma
print(df.min())  # Minimum
print(df.max())  # Maximum

print("\n__________________________PANDAS - OPERACJE NA DATAFRAME_________________________________\n")

# Operacje na DataFrame
df2 = df.copy()  # Kopiowanie DataFrame
df2['G'] = df2['A'] + df2['B']  # Dodawanie nowej kolumny
print(df2)
df2.drop('G', axis=1, inplace=True)  # Usuwanie kolumny
print(df2)
df2.drop(0, axis=0, inplace=True)  # Usuwanie wiersza
print(df2)

print("\n__________________________PANDAS - IMPORT I EKSPORT DANYCH_________________________________\n")

# Import i eksport danych
df.to_csv('data.csv', index=False)  # Eksport do pliku CSV
df.to_excel('data.xlsx', index=False)  # Eksport do pliku Excel
df = pd.read_csv('data.csv')  # Import z pliku CSV
df = pd.read_excel('data.xlsx')  # Import z pliku Excel