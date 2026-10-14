
words = ["python", "generator", "yield", "code", "ai", "developer"]

new_words = list(map(lambda word: word.upper(), filter(lambda word: len(word) > 4, words)))

# print(new_words)

for word in new_words:
    print(word)
     




