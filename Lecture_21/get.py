import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/841bf1d034fb48b6aea9e91dae1ff3e3"

try:

    response = requests.get(f"{BASE_URL}/product_list", timeout=5)
    
    print(response)
    # response.raise_for_status()
    # print(response.status_code) ესეც პასუხს ბეჭდავს
    products = response.json()

    for product in products:
        print(f"Name: {product['name']}, Price: {product['price']}, Unique ID: {product['_id']}")

    response = requests.get(f"{BASE_URL}/product_list/6ae7501a5974d603e83ceee5", timeout=5)
    # response.raise_for_status()
    # print(response.status_code) ესეც პასუხის კოდს ბეჭდავს
    print(response)
    data = response.json()
        
    print(data)
    print(f"Name: {data['name']}")
    print(f"Prince: {data['price']}")
    print(f"In stock: {data["in_stock"]}")

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")
