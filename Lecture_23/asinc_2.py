import aiohttp
import asyncio

posts_url = "https://jsonplaceholder.typicode.com/posts/{id}"


async def fetch_data(session, url):
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


async def main():
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch_data(session, posts_url.format(id=i)) for i in range(1, 21)])
      
        for response in responses:
            print(response["title"])

if __name__ == "__main__":
    asyncio.run(main())