import string
inpt = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."
words = dict()

for word in inpt.split():
    word = word.translate(word.maketrans('', '', string.punctuation)).lower()
    if str.isdigit(word):
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
word = [ [val,key] for key,val in words.items()]
word.sort()
print(f"Word appearing minimum times {word[0][1]};{word[0][0]}")
print(f"Word appearing maximum times {word[len(word)-1][1]};{word[len(word)-1][0]}")