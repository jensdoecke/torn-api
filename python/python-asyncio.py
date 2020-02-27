import asyncio
import aiohttp

api_key = '' # <- put your secret here 
id = 2200962

async def fetch(session, url, params):
    async with session.get(url, params=params) as response:
        data = await response.json()
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        url = f'https://api.torn.com/user/{id}'
        params = {'selections': 'crimes', 'key': api_key}
        data = await fetch(session, url, params)
        print(data) # do somethine with your data

# Python 3.5.3 or newer
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# Python 3.7 or newer
# asyncio.run(main())