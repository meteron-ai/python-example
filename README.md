# Python Meteron AI examples

This repository contains examples of how to use the Meteron AI API to perform basic operations.

## Requirements

- Python 3.6 or higher
- Meteron AI API key, get one [here](https://app.meteron.ai/?tab=API%20Keys)
- Add a model to your account (follow the steps in the [dashboard](https://app.meteron.ai/?tab=Settings) to add an example one)

## To generate an image

```shell
python generate.py
```

or:

```python
METERON_API_KEY = os.getenv('METERON_API_KEY')
METERON_MODEL = os.getenv('METERON_MODEL', "stable-diffusion")

url = "https://app.meteron.ai/api/images/generations"

payload = {"prompt": "futuristic city, extra detailed"}
headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + METERON_API_KEY,
	"X-Model": METERON_MODEL,
	"X-Async": "false",
  "X-User": "user-id-1"
}

response = requests.post(url, json=payload, headers=headers)
```

## To list generated images:

```python
METERON_API_KEY = os.getenv('METERON_API_KEY')
METERON_MODEL = os.getenv('METERON_MODEL', "stable-diffusion")

url = f'https://app.meteron.ai/api/images/generations?model={METERON_MODEL}&pageSize={50}'

headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + METERON_API_KEY,
}

response = requests.get(url + f"&pageToken={page_token}", headers=headers).json()

```

When listing for a particular user:

```python
METERON_MODEL = "stable-diffusion"
USER = "john-doe@example.com"

url = f'https://app.meteron.ai/api/images/generations?model={METERON_MODEL}&user=${USER}&pageSize={50}'
```