import os
import requests

METERON_API_KEY = os.getenv('METERON_API_KEY')
METERON_MODEL = os.getenv('METERON_MODEL', "stable-diffusion")

url = f'https://app.meteron.ai/api/images/generations?model={METERON_MODEL}&pageSize={20}'

headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + METERON_API_KEY,
}

generated_images = []
new_results = True
page_token = ''

'''
Response from the API is paginated. 
{
	"results": [
		...		
	],
	"pagination": {
		"pageSize": 20,
		"nextPageToken": "next-page-token-here",
		"previousPageToken": ""
	}
}
'''
while True:
  response = requests.get(url + f"&pageToken={page_token}", headers=headers).json()
  # Append the results
  new_results = response.get("results", [])  
  generated_images.extend(new_results)
  
  # Get the next page token
  page_token = response["pagination"].get('nextPageToken', '')
  
  # If there are no results, break the loop
  if not page_token:
    break
  
print(f"Total pages: {len(generated_images)}")
print(generated_images[0])