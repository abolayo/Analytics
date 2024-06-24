import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

Data = requests.get(url)
response = Data.text
article_title = []
article_rate = []
article_link = []

soup = BeautifulSoup(response, 'html.parser')
titles = soup.find_all(name='span', class_='titleline')

for title in titles:
    text = title.getText("a")
    article_title.append(text)
    link = title.find('a')
    article_link.append(link.get('href'))

rates = soup.find_all(name='span', class_='score')
for rate in rates:
    rate = rate.text
    article_rate.append(int(rate.split()[0]))

largest_number = max(article_rate)
index_largest = article_rate.index(largest_number)


print(article_link[index_largest])
print(article_rate[index_largest])
print(article_title[index_largest])

