#########################################################################
#                      Plagiat Checker 
#########################################################################

#Importe
import hashlib

#Erstellen von Shingles
def create_shingles(text, k=2): 
    shingles = set()
    text = text.replace(" ", "")  # Entfernen von Leerzeichen
    for i in range(len(text) - k + 1):
        shingle = text[i:i + k]
        shingles.add(hashlib.sha1(shingle.encode('utf-8')).hexdigest())  # Hashen mit SHA-1
    return shingles

# Test an Beispielzeile
if __name__ == "__main__":
    text1 = "Hallo Ich bin toll"
    text2 = "Hallo ich bin cool"
    shingles_set1 = create_shingles(text1, k=5)
    shingles_set2 = create_shingles(text2, k=5)
    print(" Die Shingles sind:", shingles_set1)
    print(" Anzahl der Shingles:", len(shingles_set1))
    print(" Die Shingles sind:", shingles_set2)
    print(" Anzahl der Shingles:", len(shingles_set2))

    
'''
# Test an articles.txt
if __name__ == "__main__":
    file_path = "C:\Code\Fortg. Algo\Aufgabe 3\articles.txt"
    shingles = create_shingles(file_path, k=5)
    print(" Die Shingles sind:", shingles)
'''
