import os
import aiohttp
import json
import asyncio

api_key = '3Vs4iFu6HeSNsQl1' # <- put your secret here 
id = 206

async def call_api():
    session = aiohttp.ClientSession()
    params = {'selections': 'item', 'key': api_key}
    async with session.get(f'https://api.torn.com/torn/{id}', params=params) as resp:
        data = await resp.json()
        print(data)
    await session.close()


async def main():
    print("hello")
    await call_api()


asyncio.run(main())