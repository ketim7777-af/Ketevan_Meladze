
def writter_and_quote():
    writter = input("Enter your favorite writter: ")
    quote = input("Enter your favorite qoute: ")

    return f"Favotire writter: {writter}\nFavotire quote: {quote}"

result = writter_and_quote()  

with open("quotes.txt", "w") as file:
    content = file.write(result)



try:

    with open ("quotes.txt", "r") as new_file:
        content = new_file.read()
        
        print(content)

except:
    print("File does not exist.")
