
import time
import requests
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://jsonplaceholder.typicode.com/posts/{id}"


def fetch_info(task, post_id):
    print(f"Fetching data from {task}...")

    response = requests.get(BASE_URL.format(id=post_id))
    return response.json()

start = time.time()

task_names = [f"Task{i}" for i in range(1, 101)]
post_ids = range(1, 101)

with ThreadPoolExecutor(max_workers=15) as executor:
    results = list(executor.map(fetch_info, task_names, post_ids))

end = time.time()

print(f"Total time taken: {end - start}")
print(f"Number of results: {len(results)}")
