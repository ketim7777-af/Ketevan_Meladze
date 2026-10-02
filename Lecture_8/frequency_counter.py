words =  ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
    
print(word_counts)

for key, value in word_counts.items():
    if value > 1:
        print(f"{key}")
        
       





