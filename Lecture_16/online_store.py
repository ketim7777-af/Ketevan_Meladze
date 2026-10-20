class Products:
    shop_name = "MegaShop"
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, quantity):
        self.stock -= quantity
        print(f"Sold {quantity} {self.name}, remaining: {self.stock}")
       
    def display(self):
           
        print(f"Shop nema: {self.shop_name}")
        print(f"Product name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        
            

product_1 = Products("Leptop", "2500 L", 3)
product_1.sell(2)
product_1.display()

print("=" *30)

product_2 = Products("PC", "4500 L", 1)
product_2.sell(1)
product_2.display()

print("=" *30)

product_3 = Products("Pad", "95 L", 5)
product_3.sell(2)
product_3.display()

