from dataclasses import dataclass

@dataclass
class Product:
   name: str
   priece: int
   in_stock: bool

product_1 = Product("Ball", 25, True)    
product_2 = Product("Dall", 125, True)
product_3 = Product("Trousers", 225, False)   

print(product_1)
print(product_2)
print(product_3)
