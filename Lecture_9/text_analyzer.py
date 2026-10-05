
def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = []
    words = text.split()  
    count = 0

    for word in words:
        if len(word) >= min_length and words not in ignore_stopwords:
            count +=1

    return count


print(analyze_text("My name is Keti"))

# ასეც შეიძლება:

result = analyze_text("My full name is Ketevan and short one is Keti")
print(result)