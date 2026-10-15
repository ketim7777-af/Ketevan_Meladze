
words = ["python", "generator", "yield", "code", "ai", "developer"]

def new_words():
    yield list(map(lambda word: word.upper(), filter(lambda word: len(word) > 4, words)))

for word in new_words():
    print(word)

     




