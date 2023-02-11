from fuzzywuzzy import fuzz
from nltk.metrics.distance import edit_distance

a = ["apple", "banana", "cherry"]
b = ["apple", "banana", "pear"]
c = ["apple", "banana", "cherry"]

def similarity(a, b):
    nltk_ratio = 1 - (edit_distance(a, b) / max(len(a), len(b)))
    fuzz_ratio = fuzz.ratio(a, b)/100
    return (fuzz_ratio+nltk_ratio)/2

print("Similarity ratio between a and b:", similarity(a,b))
print("Similarity ratio between a and c:", similarity(a,c))
