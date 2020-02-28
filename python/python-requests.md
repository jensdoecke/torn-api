# Python GET with 'requests' module

Create Directory

```bash
mkdir my_app && cd my_app
```

Create Virtual Env

```bash
python3 -m venv venv
```

Activate Virtual Env

```bash
source venv/bin/activate
```

Install Modules with pip

```bash
pip install requests
```

Example of requests call:

```python
import requests

api_key = '' # <- put your secret here
id = 2200962


def fetch(url, params):
    response = requests.get(url, params=params)
    return response.json()

url = f'https://api.torn.com/user/{id}'
params = {'selections': 'crimes', 'key': api_key}
data = fetch(url, params)
print(data) # do somethine with your data
```
