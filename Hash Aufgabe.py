import csv

file_path = "C:\Users\lukib\Downloads\de.DE.csv"


def read_csv_file(file_path):
    rows = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        csv_reader = csv.reader(file)
        row_count = 0
        for row in csv_reader:
            rows.append(row)
            row_count += 1
            if row_count == 100000:
                break
    return rows

rows = read_csv_file(file_path)

hashsize = 100000
def hash(string):
    summe = 0
    for buchstabe in string: 
        summe += ord(buchstabe)
    return summe % hashsize 


hashliste = set()
dublikat = []

for row in rows:
    hashwert = hash(str(row))
    if hashwert in hashliste:
        dublikat.append(hashwert)
    else:
        hashliste.add(hashwert)

if dublikat:
    print("Folgender Wert ist ein Dublikat")
    for wert in dublikat:
        print(wert)
else: 
    print("Keine Dublikate gefunden") 
