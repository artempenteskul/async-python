import requests
from time import time


URL = 'https://loremflickr.com/320/240'


"""
sync example of 100 files download
"""


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(f'media/{filename}', 'wb') as f:
        f.write(response.content)


def main():
    start = time()

    for i in range(100):
        write_file(get_file(url=URL))

    print(time() - start)


if __name__ == '__main__':
    main()


######################
######################
######################


"""
async example of 100 files download
"""

import asyncio
import aiohttp


def write_image(data):
    filename = f'media/file-{str(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            task = asyncio.create_task(fetch_content(URL, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time()
    asyncio.run(main2())
    print(time() - start)
