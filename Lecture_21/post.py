import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/841bf1d034fb48b6aea9e91dae1ff3e3"

try:

    product_list = {
        "name": "Laptop",
        "price": 2500,
        "in_stock": True
    }

    response = requests.post(f"{BASE_URL}/product_list", json = product_list, timeout=5)
    # response.raise_for_status()   
    # print(response.status_code)  ესეც პასუხს ბეჭდავს
    print(response)
    
    print(response.json())

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")

