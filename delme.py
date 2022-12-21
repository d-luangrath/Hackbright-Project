import requests
import os

# url = "https://api.spoonacular.com/recipes/random"

# api_key = os.environ.get("SPOONACULAR_API_KEY", None)
# if not api_key:
#     raise Exception("API key is not found. Did you forget to export it?")

# payload = {'number': 1}
# headers = {'x-api-key': api_key}

# response = requests.request("GET", url, headers=headers, data=payload)

api_key = os.environ.get("SPOONACULAR_API_KEY", None)
if not api_key:
    raise Exception("API key is not found. Did you forget to export it?")

url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"

payload = {'number': 3}

response = requests.request("GET", url, params=payload)

recipes = response.json()['recipes'] # list
print(len(recipes))

