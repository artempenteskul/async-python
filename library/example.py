import asyncio


counter = 0


async def print_counter():
    global counter

    while True:
        print(counter)


async def func1():
    global counter

    while True:
        counter += 1
        counter -= 1
        await asyncio.sleep(1)


async def func2():
    global counter

    while True:
        counter += 1
        counter -= 1
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.gather(func1(), func2(), print_counter())
    asyncio.get_event_loop().run_forever()
