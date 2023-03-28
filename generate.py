import requests
import os
import shutil
from urllib import request


METERON_API_KEY = os.getenv('METERON_API_KEY')

url = "https://app.meteron.ai/api/images/generations"

payload = {"prompt": "futuristic city, extra detailed"}
headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + METERON_API_KEY,
	"X-Model": "stable-diffusion",
	"X-Async": "false",
  "X-User": "user-id-1"
}

response = requests.post(url, json=payload, headers=headers)

response_json = response.json()

print(response_json["outputImages"][0]["url"])

# Download the image. The response contains JSON with base64 encoded
# image data such as:
#   {"image":"data:image/png;base64,iVBORw..."}
image_response = requests.get(response_json["outputImages"][0]["url"])

with request.urlopen(image_response.json()["image"]) as data:
  with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(data, out_file)
