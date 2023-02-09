import string
from nltk.stem.snowball import SnowballStemmer  

stemmer = SnowballStemmer("romanian")

# elimina orice symbol care nu e o litera sau cifra
def remove_punctuations(token:str):
    return token.translate(str.maketrans("", "", string.punctuation))

def process(input_string:str):
    # o lista cu toate cuvintele care trebe scoase din inputul userului
    cuvinte_de_stopare= open("./AIChatApp/SugestiiAI/cuvinte_de_stopare.csv","r").read().split(",")
    
    # facem toate literele mici si destructuram stringul in o lista de cuvinte/token-uri
    input_string = input_string.lower().split(" ")

    # filtram fiecare token in ormatorul mod: 
    # 1. verificam daca se afla in cuvinte de stopare, daca da, il ignoram
    # 2. il curatam de semne de punctuatie
    # 3. il extragem radacina
    input_string = [stemmer.stem(remove_punctuations(token)) for token in input_string if token not in cuvinte_de_stopare]
    
    return input_string

# print(process("Salutare, aceasta este pisicuta mea"))
# # output: ['salut', 'pisic']