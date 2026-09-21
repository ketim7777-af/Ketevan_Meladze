first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
print(first_name, last_name)

text = "My favorite thing is Python"
print(text.replace("thing", "language"))
text = text.replace("thing", "language")
print(text.find('Python'))
print(text[12:])

name = input("Enter your name:")
company = input("Enter your company name:")
print(f"Hello {name}, your workplace is {company}.")