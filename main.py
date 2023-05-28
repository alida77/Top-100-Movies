import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")

raw_movies = soup.find_all(name="h3")
movies = []
for movie in raw_movies:
    movies.append(movie.getText())

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed(movies):
        file.write(f"{movie}\n")
