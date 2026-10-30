import json

json_data = '{"name": "Laptop", "price": 2500, "in_stock": true}'

python_data = json.loads(json_data)

from dataclasses import dataclass, asdict

@dataclass
class Products:
   name: str
   price: int
   in_stock: bool

restored_product = Products(**python_data)

print(python_data)
