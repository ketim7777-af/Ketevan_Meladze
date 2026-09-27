
inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grape"]

print(inventory.count("apple"))  
print(inventory.index("orange"))
#  დავალებაში დათვალე და იპოვე წერია, მაგრამ მე დავპრინტე კიდეც

inventory.extend(new_items)
print(inventory[:: -1])