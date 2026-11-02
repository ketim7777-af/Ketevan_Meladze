import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/841bf1d034fb48b6aea9e91dae1ff3e3"

try:

    response = requests.delete(f'{BASE_URL}/product_list/6ae76c4c43d3af03e8e61931', timeout=5)
    response.raise_for_status()
    print(response.status_code)
    # print(response)

    if 200 <= response.status_code < 205:
        print("Product was deleted.")


except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")