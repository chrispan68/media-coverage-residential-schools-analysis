import requests
import json

API_KEY = "569e452a-9e77-4688-8740-f59df51999c5"
ALL_URL = f"https://api.goperigon.com/v1/all?apiKey={API_KEY}"

resp = requests.get(f"{ALL_URL}&q=%22residential%20school%22&sourceGroup=top100&from=2021-05-01&to=2021-07-31&size=100&page=1")
articles = resp.json()

with open('news-articles-residential-school-page1.json', 'w') as f:
    json.dump(articles, f, indent=4)