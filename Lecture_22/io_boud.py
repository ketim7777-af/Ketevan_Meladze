
import time
import threading
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/posts/{id}'

def fetch_info(task, post_id):
    print(f"Fetching data from {task}...")

    response = requests.get(BASE_URL.format(id=post_id))
    return response.json()

start = time.time()

thread_list = []

for i in range(1, 101):
    
    thread = threading.Thread(target=fetch_info, args=(f"Task{i}", i))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end = time.time()
print(f"Total time taken: {end - start}")