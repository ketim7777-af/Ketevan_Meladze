age = int(input("Enter your age:"))
if age >= 65:
    print("Your ticket price is $10")
elif age >= 13:
    print("Your ticket price is $15")
elif age >= 5:
    print("Your ticket price is $8")
elif age >= 0:
    print("Your ticket price is $0")
else:
    print("invalid age entered")