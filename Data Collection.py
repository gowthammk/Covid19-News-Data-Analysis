from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
import requests
import os.path
from datetime import timedelta, date
from  newspaper import Article

def newsscrape(keyword, api_key, date):

    parameters_coronavirus = {
        'q' : keyword,
        'pageSize' : 100,
        'apiKey' : api_key,
        'language' : 'en',
        'from' : date
    }
    request = requests.get(url, params = parameters_coronavirus)
    response = request.json()
    data = response["articles"]
    current_date = date.today()
    day = current_date.strftime('%A')
    today = str(current_date) + " " + day
    count = 0
    for i in range(1, len(data)):
        try:
            website_name = (data[i]["source"]["name"])
            headline = (data[i]["title"])
            description = (data[i]["description"])
            link = (data[i]["url"])
            article = Article(link)
            article.download()
            article.html
            article.parse()
            content = article.text
            content_title = article.title
            date = (data[i]["publishedAt"])

        except Exception as e:
            website_name = str(None)
            headline = str(None)
            description = str(None)
            link = str(None)
            content = str(None)
            date = str(None)
        file_exist = os.path.isfile(keyword + " " + 'News ' + today +  " " + str(count) + " " + '.txt')
        file = open(keyword + " " + 'News ' + today + " " + str(count) + " " + '.txt', 'a', newline="", encoding='utf-8')
        file.write(headline)
        file.write(description)
        file.write(content)
        count += 1
    file.close()
if __name__ == "__main__":
    newsapi = NewsApiClient(api_key='API_KEY')
    url = "https://newsapi.org/v2/everything?"
    api_key = "6bdbee3c4161470b82c76bc00e179186"
    keyword = ["coronavirus vaccine", "covid19 vaccine"]
    for i in keyword:
        date = (date.today() + timedelta(days=-30))
        newsscrape(i, api_key, date)