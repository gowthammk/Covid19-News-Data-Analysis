import os
import re

files = []
for dirname, _, foldernames in os.walk("C:\\Users\\Gowtham\\PycharmProjects\\Covid19-News-Data-Analysis\\Dataset"):
    for foldername in foldernames:
        files.append(dirname + "\\"+foldername)


with open("C:\\Users\\Gowtham\\PycharmProjects\\Covid19-News-Data-Analysis\\Dataset\\output_file.txt", "w", encoding = "utf8") as outfile:
    for filename in files:
        file = open(filename, encoding="utf8")
        with file as infile:
            outfile.write(file.read() + "\n\n\n\n")


def cleanText(text):
    try:
        # remove links, unwanted texts, special characters in the text
        text=re.sub(r'@[A-Za-z0-9]+','',text)
        text=re.sub(r'#','',text)
        text=re.sub(r'RT[\s]+','',text)
        text=re.sub(r'https?:\/\/\S+','',text)
        text=re.sub(r'[^\w]', ' ', text)
        text = re.sub(r"Advertisement" , "", text)
        text  = re.sub(r"\n\s*\n","", text)
    except:
        pass
    return text
with open("C:\\Users\\Gowtham\\PycharmProjects\\Covid19-News-Data-Analysis\\Dataset\\output_file.txt", "r", encoding = "utf8") as f:
    for i in f:
        with open('C:\\Users\\Gowtham\\PycharmProjects\\Covid19-News-Data-Analysis\\Dataset\\clean_file.txt', 'a', encoding = "utf8") as the_file:
            the_file.write(cleanText(i) + "\n")


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=open ('C:\\Users\\Gowtham\\PycharmProjects\\Covid19-News-Data-Analysis\\Dataset\\clean_file.txt', encoding = "utf8").read()

wordcloud = WordCloud(stopwords = STOPWORDS,
                            background_color = 'white',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func
                            ).generate(file_content)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()