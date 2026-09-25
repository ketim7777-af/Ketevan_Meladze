text = input("Enter text: ")

for symbol in text:
    if symbol.isdigit():
        continue
    print(symbol, end="")


