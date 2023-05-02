import requests
import json

api_key = "ee82603e140342af8eb68c4119307ab0"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-04-02&sortBy=publishedAt&api" \
      "Key=ee82603e140342af8eb68c4119307ab0"

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article["title"])
    print(article['description'])