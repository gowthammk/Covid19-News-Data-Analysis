import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import csv
import os.path

# url definition
url = "https://www.bbc.com/news/coronavirus"

# Request
r1 = requests.get(url)

# We'll save in coverpage the cover page content
coverpage = r1.content
# Soup creation
soup = BeautifulSoup(coverpage, 'lxml')

#def create_csv_file():
#CSV File create and write header
file_exist = os.path.isfile('./BBC_Scrape.csv')
csv_file = open('BBC_Scrape.csv', 'w', newline="", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'News Link', 'News Title', 'News Summary'])


# BBC news page has two section -  Cover page news and Latest news

#coverpage_news() is to deal with the Cover page news section
def coverpage_news():
    #Reading the entire coverpage news content
    coverpage_news = soup.find_all('a',
                                   class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')

    for n in np.arange(0, len(coverpage_news)):
        # Getting the headline of the article
        headline = coverpage_news[n].h3.text
        summary = soup.find_all('p',
                                class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m")
        #Gets all the links related to the article
        links = coverpage_news[n]['href']

        try:
            #Insert "https://www.bbc.com/" manually if not already present
            url_header = "https://www.bbc.com/"
            if (url_header in links):
                link = links
            else:
                link = url_header + links
            #Getting all the contents in the Cover page news
            news_contents = summary[n].get_text()

        except Exception as e:
            news_contents = None
            article_summary = None

        #Reading the article in the link obtained in the coverpage
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'lxml')
        #Getting the headline of the article in the link in the coverpage
        article_title = soup_article.title.text
        article_ = soup_article.find_all('p')
        list_paragraph = []
        article_body = []

        # Getting the content in the article of the link in the coverpage
        for a in range(0, len(article_)):
            article_paragraph = article_[a].get_text()
            list_paragraph.append(article_paragraph)
            article_summary = " ".join(list_paragraph)
        article_body.append(article_summary)

        csv_writer.writerow([headline, news_contents, link, article_title, article_summary])


#latest_news() is to deal with the latest news section
def latest_news():
    #Reading the entire latest news content
    latest_news = soup.find_all("article",
                                class_="lx-stream-post gs-u-align-left lx-stream-post--has-meta")

    for n in np.arange(0, len(latest_news)):
        try:
            # Getting the headline of the article
            headline = latest_news[n].h3.text
            news_contents = latest_news[n].p.text
            # Gets all the links related to the article
            link = latest_news[n].a['href']
            url_header = "https://www.bbc.com/"
            if (url_header in link):
                link = link
            else:
                link = url_header + link

        except Exception as e:
            headline = None
            news_contents = None
            link = None

        # Reading the article in the link obtained in the latest news page
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'lxml')
        # Getting the headline of the article in the link in the latest news page
        article_title = soup_article.title.text
        article_ = soup_article.find_all('p')
        list_paragraph = []
        article_body = []

        # Getting the content in the article of the link in the latest news page
        for a in range(0, len(article_)):
            article_paragraph = article_[a].get_text()
            list_paragraph.append(article_paragraph)
            article_summary = " ".join(list_paragraph)
        article_body.append(article_summary)

        csv_writer.writerow([headline, news_contents, link, article_title, article_body])


#Main function
if __name__ == "__main__":
    coverpage_news()
    latest_news()
    csv_file.close()