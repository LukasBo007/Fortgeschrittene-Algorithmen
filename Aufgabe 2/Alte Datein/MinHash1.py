import hashlib

# Anzahl der Hashfunktionen für MinHash
anzahl_hashfunktionen = 100

# Funktion, um Shingles aus einem Text zu erstellen
def create_shingles(text, k=2):
    words = text.split()
    shingles = set()
    for i in range(len(words) - k + 1):
        shingle = " ".join(words[i:i + k])
        shingles.add(shingle)
    return shingles

# Funktion, um MinHash-Signaturen für eine Menge von Shingles zu erstellen
def minhash_signature(shingles, anzahl_hashfunktionen):
    minhash_values = []
    for i in range(anzahl_hashfunktionen
):
        minhash_value = float('inf')
        for shingle in shingles:
            # Verwende eine Hashfunktion, um den Hashwert für das Shingle zu berechnen
            hash_value = hashlib.md5((str(i) + shingle).encode()).hexdigest()
            # Konvertiere den Hexadezimalwert in eine Ganzzahl und aktualisiere den Minhash-Wert
            hash_int = int(hash_value, 16)
            minhash_value = min(minhash_value, hash_int)
        minhash_values.append(minhash_value)
    return minhash_values

# Funktion, um die Ähnlichkeit zwischen zwei MinHash-Signaturen zu berechnen
def minhash_similarity(signature1, signature2):
    matching_hashes = sum(sig1 == sig2 for sig1, sig2 in zip(signature1, signature2))
    return matching_hashes / anzahl_hashfunktionen


# Funktion zum Finden von Plagiaten in einer Liste von Sätzen
def find_plagiarism(sentences):
    signatures = []
    plagiarized_pairs = []
    
    # Erstelle MinHash-Signaturen für jeden Satz
    for sentence in sentences:
        shingles = create_shingles(sentence)
        signature = minhash_signature(shingles, anzahl_hashfunktionen
    )
        # Überprüfe auf Plagiate mit anderen Sätzen
        for i, (existing_signature, existing_sentence) in enumerate(signatures):
            similarity = minhash_similarity(signature, existing_signature)
            # Wenn Ähnlichkeit höher als ein Schwellenwert, markiere als Plagiat
            if similarity > 0.8:
                plagiarized_pairs.append((existing_sentence, sentence))
        signatures.append((signature, sentence))
    
    return plagiarized_pairs

# Beispielaufruf
sentences = ["The lazy dog jumps over the fence.",
             "A quick brown fox jumps over the lazy dog.",
             "The lazy dog jumps over the wall.",
             "A brown dog jumps over the lazy fox.",
             "The lazy cat jumps over the fence."]

plagiarized_pairs = find_plagiarism(sentences)
print("Plagiatpaare gefunden:")
for pair in plagiarized_pairs:
    print(pair)
