#########################################################################
#                      Plagiat Checker 
#########################################################################

#Vergleich  mit Allen

#Importe
import hashlib

def shingle_text(text, k):
    shingles = set()
    words = text.split()

    for i in range(len(words) - k + 1):
        shingle = " ".join(words[i:i+k])
        shingles.add(hash(shingle) % (2**32 - 1))

    return shingles

def minhash(signature_size, shingles):
    hash_values = [float('inf')] * signature_size

    for shingle in shingles:
        for i in range(signature_size):
            hash_val = hash(str(shingle) + str(i)) % (2**32 - 1)
            hash_values[i] = min(hash_values[i], hash_val)

    return hash_values

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    return intersection / union

def find_similar_lines(file_path, k, signature_size, similarity_threshold):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        lines = text.splitlines()

    plagiate_gefunden = False  # Variable, um festzustellen, ob Plagiate gefunden wurden
    anzahl_plagiate = 0  # Variable zur Zählung der Plagiate

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            shingles1 = shingle_text(lines[i], k)
            shingles2 = shingle_text(lines[j], k)

            signature1 = minhash(signature_size, shingles1)
            signature2 = minhash(signature_size, shingles2)

            similarity = jaccard_similarity(set(signature1), set(signature2))

            if similarity > similarity_threshold:
                print(f"Similarity between lines {i+1} and {j+1}: {similarity * 100:.2f}%")
                plagiate_gefunden = True
                anzahl_plagiate += 1

    if plagiate_gefunden:
        print(f"Anzahl aller Plagiate: {anzahl_plagiate}")
    else:
        print("Es wurden keine Plagiate gefunden")

file_path = "articles.txt"
find_similar_lines(file_path, k=5, signature_size=100, similarity_threshold=0.0)
