import time
import requests
import aiohttp
import asyncio

rick_morty_url = "https://rickandmortyapi.com/api/character/{id}"


def fetch_data():
    characters = []

    for i in range(1, 11):
        url = rick_morty_url.format(id=i)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        characters.append(response.json())

    return characters


async def fetch_character(session, url):
    try:
        timeout = aiohttp.ClientTimeout(total=10)

        async with session.get(url, timeout=timeout) as response:
            response.raise_for_status()
            return await response.json()

    except aiohttp.ClientResponseError as e:
        print(e)

    except aiohttp.ClientConnectionError as e:
        print(e)

    except aiohttp.ContentTypeError as e:
        print(e)

    except asyncio.TimeoutError as e:
        print(e)

    except Exception as e:
        print(e)

    return None


async def main():
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            *[
                fetch_character(session, rick_morty_url.format(id=i)) for i in range(1, 11)])

    return responses


start_time1 = time.time()
characters = fetch_data()
end_time1 = time.time()
requests_time = end_time1 - start_time1

start_time2 = time.time()
async_characters = asyncio.run(main())
end_time2 = time.time()
async_time = end_time2 - start_time2

difference = requests_time - async_time
print(f"The async method is faster by {difference:.2f} seconds.")