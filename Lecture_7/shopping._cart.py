try:
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    total = price * quantity

except ValueError:
    print("Error: Both price and quantity must be valid numbers!")

else:
    print(f"Total price: ${total:.2f}.")





