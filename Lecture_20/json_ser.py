

from dataclasses import dataclass, asdict

@dataclass
class Product:
   name: str
   price: int
   in_stock: bool

product_1 = Product("Ball", 25, True)    
product_2 = Product("Dall", 125, True)
product_3 = Product("Trousers", 225, False)   

python_data1 = asdict(product_1)
python_data2 = asdict(product_2)
python_data3 = asdict(product_3)

import json
json_data1 = json.dumps(python_data1, indent = 4)
json_data2 = json.dumps(python_data2, indent = 4)
json_data3 = json.dumps(python_data3, indent = 4)

print(json_data1)
print(json_data2)
print(json_data3)
