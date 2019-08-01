import string
try:
    count = 0
    word_count = dict()
    with open("text.txt") as f:
        data = f.readlines()
        for line in data:
            words =  line.translate(line.maketrans('', '', string.punctuation)).lower().split()
            count += len(words)
            for word in words:
                # word = word.lower()
                word = word.translate(word.maketrans('', '', string.punctuation)).lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    print(f"The no.of words are {count}")
    word_list = [ (val,key) for key,val in word_count.items() ]
    word_list.sort()
    print(f"The most used word is {word_list[-1][1]} and count is {word_list[-1][0]}")
    print(f"The least used word is {word_list[0][1]} and count is {word_list[0][0]}")
    print(f"Conjunctuions : and -{word_count['and'] if 'and' in word_count else 0} , but - {word_count['but'] if 'but' in word_count else 0} , if - {word_count['if'] if 'if' in word_count else 0}")
except Exception as e:
    print(e)

