
try:
    fruits = ["apple", "banana", "cherry", "orange"]
    index = int(input("Enter the index: "))
    print(f"Selected fruit: {fruits[index]}")

except ValueError:
    print("Wrong format. Please enter the whole number!")

except IndexError:
   print(f"Index is out of range! Choose an index starting from 0 to {len(fruits)-1}")

else:
    print("The item was found successfully!")  