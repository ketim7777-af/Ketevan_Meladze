import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/841bf1d034fb48b6aea9e91dae1ff3e3"

try:

    updated_products = {
        "name": "Gaming Laptop",
        "price": 3200,
        "in_stock": True
    }

    response = requests.put(f'{BASE_URL}/product_list/6ae7501a5974d603e83ceee5', json=updated_products, timeout=5)
    # response.raise_for_status()
    # print(response.status_code)
    print(response)

    updated_response = requests.get(f"{BASE_URL}/product_list/6ae7501a5974d603e83ceee5")
    updated_data = updated_response.json()
    # response.raise_for_status()
    # print(response.status_code)
    
    print(updated_data)
    print(f"Name: {updated_data['name']}")
    print(f"Prince: {updated_data['price']}")
    print(f"In stock: {updated_data["in_stock"]}")
    print(response)

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")
