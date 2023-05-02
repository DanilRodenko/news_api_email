import requests
from send_mail import send_mail


topic = "tesla"
api_key = "ee82603e140342af8eb68c4119307ab0"
url = "https://newsapi.org/v2/everything" \
      f"?q={topic}" \
      "&from=2023-04-02&" \
      "sortBy=publishedAt&" \
      "apiKey=ee82603e140342af8eb68c4119307ab0&" \
      "language=en"

request = requests.get(url)
content = request.json()
message = ''
for article in content['articles'][:20]:
    if article["title"] is not None:
        message = "Subject: Today News" \
                  + "\n" + message + article['title']\
                  + "\n" + article['description']\
                  +'\n' + article['url'] + 2*'\n'

send_mail(message=message)

