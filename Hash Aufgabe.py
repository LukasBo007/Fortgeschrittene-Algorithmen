import csv
import matplotlib.pyplot as plt
import numpy as np

"""TODO: 1. Anzahl der Tabellengröße bei der Ausführung der Funktion bestimmen können, 
2. Anzahl der Inputwerte bestimmen
3. gleichzeitig verändert sich die Länge des Mittelwertes in der midquare methode. 
4. Histogramm bauen """



def read_csv_file(file_path):
    rows = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        csv_reader = csv.reader(file)
        row_count = 0
        for row in csv_reader:
            rows.append(row)
            row_count += 1
            if row_count == 50: 
                break
    return rows

def key_Wert(input_Wert):
    key = 0
    for buchstabe in input_Wert:
        key += ord(buchstabe)
    return key  # Die Rückgabe sollte außerhalb der Schleife erfolgen

def mid_square_hash(input_key: int):
    hashsize = 1000
    squared = input_key * input_key
    str_squared = str(squared)
    length = len(str_squared)
    start = (length - 3) // 2
    end = start + 3
    mid_value = int(str_squared[start:end])
    return mid_value % hashsize

file_path = "/Users/furkan/Downloads/archive/de_DE.csv"
rows = read_csv_file(file_path)

hashliste = set()
dublikat = []

for row in rows:
    key = key_Wert(str(row))
    hashwert = mid_square_hash(key)
    while hashwert in hashliste:  # Wenn der Hashwert bereits existiert, behandeln Sie die Kollision
        dublikat.append(hashwert)
        hashwert = mid_square_hash(hashwert)  # Eine einfache Methode, um die Kollision zu behandeln
    hashliste.add(hashwert)

if dublikat:
    print("Folgende Werte sind Dublikate:")
    for wert in dublikat:
        print(wert)
else: 
    print("Keine Dublikate gefunden")

gaussian_numbers = np.random.normal(size= 10000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Tabelle")
plt.ylabel("Kollisionen")
plt.show()