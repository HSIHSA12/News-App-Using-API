import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "a34c0d2c256945d583fb4a4d1c9f0543"

url=f'https://newsapi.org/v2/everything?q={query}&from=2025-05-25&sortBy=publishedAt&apiKey={api}'
print(url)

r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
