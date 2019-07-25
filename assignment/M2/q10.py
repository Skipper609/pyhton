import string

inpt = "How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
words = dict()

for word in inpt.split():
    word = word.translate(word.maketrans('', '', string.punctuation)).lower()
    if str.isdigit(word):
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print(f"Unique words are {len(words)}")

for key,value in words.items():
    print(f"{key} : {value}")