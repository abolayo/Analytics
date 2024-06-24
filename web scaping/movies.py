import requests
from bs4 import BeautifulSoup

url = 'https://www.empireonline.com/movies/features/best-movies-2/'

Data = requests.get(url)
response = Data.text
list_movies = []
soup = BeautifulSoup(response, 'html.parser')
title = soup.find('h1', class_='title_h1__SREzS undefined')
print(title.getText())
movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')
for movie in movies:
    list_movies.append(movie.getText().split(" ", 1)[1])
print(list_movies)
with open('movie_file.txt', 'w') as f:
    f.write(title.getText())
    for count, line in enumerate(list_movies, 1):
        f.write(f"{count}. {line}\n")
# # OR
#
# movie_list = [movie.getText() for movie in movies]
# with open('movie_file.txt', 'w') as f:
#     f.write(f"{movie_list[::-1]}")
