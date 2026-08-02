import requests
import ytmusicapi
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/bakeboard-hot-100/2026-03-07/")
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

songs = soup.find_all(name="h3",class_="chart-entry__title")
songs_list = [song.getText() for song in songs]
print(songs_list)

