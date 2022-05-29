# Standard Library
import asyncio
import contextlib
import time

# Third Party
import aiohttp

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(pokemon["name"])


async def req(url):
    async with aiohttp.ClientSession() as session:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response


@contextlib.contextmanager
def async_loop():
    print("open loop")
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.close()
        print("close loop")


def request(url, method="GET", data=None):
    with async_loop() as loop:
        result = loop.run_until_complete(req(url))

    return result
