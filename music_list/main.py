import requests
from bs4 import BeautifulSoup
import datetime

date = input('Which year would you like to travel to? Type the date in this format: YYYY-MM-DD:').strip()

url = f'https://www.billboard.com/charts/hot-100/{date}/'

Data = requests.get(url)
response = Data.text
list_music = []
soup = BeautifulSoup(response, 'html.parser')
names = soup.select('li ul li h3')
top_100 = [name.getText().strip() for name in names]
print(top_100)

