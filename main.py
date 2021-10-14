from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = 'playlist-modify-public'
username = 'pbdadpwx30tf1zg1r9thvkrt5'

spotify_client_id = os.environ.get('SPOTIPY_CLIENT_ID')
secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

token = SpotifyOAuth(client_id=spotify_client_id, client_secret=secret, redirect_uri=redirect_uri,
                     scope=scope, username=username)
spotify_Object = spotipy.Spotify(auth_manager=token)


what_day = input('What year would you like you travel to? Type the date in this format YYYY-MM-DD: ')
memory = input('What memory do you have of this day? This will go as the playlist description. ')

chrome_driver_path = "/Users/TaylorLoatman/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(f'https://www.billboard.com/charts/hot-100/{what_day}')
song_list = driver.find_elements(By.CSS_SELECTOR, '.chart-list li .chart-element__information__song')

# create playlist
playlist_name = f'Billboard Top 100 Week {what_day}'
spotify_Object.user_playlist_create(user=username, name=playlist_name, public=True, description=memory)

#get tracks
playlist_config = []

for song in song_list:
    results = spotify_Object.search(q=song.text, limit=1, type='track')
    playlist_config.append(results['tracks']['items'][0]['uri'])

#find new playlist
pre_playlist = spotify_Object.user_playlists(user=username)
playlist = pre_playlist['items'][0]['id']

#add songs
spotify_Object.playlist_add_items(playlist_id=playlist, items=playlist_config)


driver.quit()




