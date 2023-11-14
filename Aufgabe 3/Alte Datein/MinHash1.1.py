
#Importe
import hashlib

# Anzahl der Hashfunktionen für MinHash
anzahl_hashfunktionen = 100

#Festlegen der Ähnlichkeit
#aehnlichkeit = 0.2 #Ab wann ein Paar als PLagiat zählt
while True:
    try:
        aehnlichkeit = float(input("Geben Sie die gewünschte Ähnlichkeit zwischen 0 und 1 ein: ")) #Nutzer gibt Ähnlichkeit an
        if 0 <= aehnlichkeit <= 1:
            break
        else:
            print("Ungültige Eingabe. Die Zahl muss zwischen 0 und 1 liegen.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl zwischen 0 und 1 ein.")

# Wortgruppen
file_path = "articles.txt"

# Open the file and read its contents
with open(file_path, 'r') as file:
    wortgruppen = file.read()

# Print the contents of the file
#print(wortgruppen)


# Erstellen von Shingles
def create_shingles(text, k=2): #k = Shingle Länge
    words = text.split()
    shingles = set()
    for i in range(len(words) - k + 1):
        shingle = " ".join(words[i:i + k])
        shingles.add(shingle)
    return shingles

# minHash Signaturen erstellen
def minhash_signature(shingles, anzahl_hashfunktionen):
    minhash_values = []
    for i in range(anzahl_hashfunktionen):
        minhash_value = float('inf')
        for shingle in shingles:
            hash_value = hashlib.md5((str(i) + shingle).encode()).hexdigest() # Verwende eine Hashfunktion, um den Hashwert für das Shingle zu berechnen
            hash_int = int(hash_value, 16) # Konvertiere den Hexadezimalwert in eine Ganzzahl und aktualisiere den Minhash-Wert
            minhash_value = min(minhash_value, hash_int)
        minhash_values.append(minhash_value)
    return minhash_values

# Funktion, um die Ähnlichkeit zwischen zwei MinHash-Signaturen zu berechnen
def minhash_aehnlichkeit(signature1, signature2):
    passende_hashes = sum(sig1 == sig2 for sig1, sig2 in zip(signature1, signature2))
    return passende_hashes / anzahl_hashfunktionen

# Erstelle Shingles für jede Wortgruppe
shingles_list = [create_shingles(word_group) for word_group in wortgruppen]

# Erstelle MinHash-Signaturen für jede Menge von Shingles
minhash_signatures = [minhash_signature(shingles, anzahl_hashfunktionen) for shingles in shingles_list]

# Vergleiche zwischen MinHash-Signaturen und Wortgruppen
anzahl_plagiate = 0 #Um Plagiate später zu zählen
for i in range(len(wortgruppen)):
    for j in range(i + 1, len(wortgruppen)):
        similarity = minhash_aehnlichkeit(minhash_signatures[i], minhash_signatures[j])
        if similarity >= aehnlichkeit:
            print(f"Ähnlichkeit zwischen \"{wortgruppen[i]}\" und \"{wortgruppen[j]}\": {similarity}")
            anzahl_plagiate += 1

#Anzahl Plagiate
#print(f"Gesamtzahl aller Plagiate: {anzahl_plagiate}")
#print("Gesamtzahl aller Plagiate:", len(wortgruppen))
print("Aus", len(wortgruppen), "Wortgruppen sind", anzahl_plagiate, "Plagiate")