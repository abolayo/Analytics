# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
# from _datetime import datetime
#
#
# def validate_date(input_date):
#     try:
#         datetime.strptime(input_date, "%Y-%m-%d")
#         return True
#     except ValueError:
#         return False
#
#
# date = input('Which year would you like to travel to? Type the date in this format: YYYY-MM-DD:').strip()
# if validate_date(date):
#     url = f'https://www.billboard.com/charts/hot-100/{date}/'
#
#     Data = requests.get(url)
#     response = Data.text
#     list_music = []
#     soup = BeautifulSoup(response, 'html.parser')
#     names = soup.select('li ul li h3')
#     top_100 = [name.getText().strip() for name in names]
#
# #           Spotify Authentication
# YOUR_APP_CLIENT_ID = "85672c3adaee477ca718f88312b7a6b6"
# YOUR_APP_CLIENT_SECRET = "1034602c10984f658654b6241cd002db"
# YOUR_APP_REDIRECT_URI = "http://example.com"
#
#
# # Now creating playlist in spotify
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
#                                                client_secret=YOUR_APP_CLIENT_SECRET,
#                                                redirect_uri=YOUR_APP_REDIRECT_URI,
#                                                scope="playlist-modify-private",
#                                                show_dialog=True,
#                                                cache_path=".cache"
#                                                ))
#
# results = sp.current_user()
# user_id = results['id']
# print(f"USER_ID is {user_id}")
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# song_names = ["The list of song", "titles from your", "web scrape"]
#
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#
# #Adding songs found into the new playlist


from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
YOUR_CLIENT_ID = "85672c3adaee477ca718f88312b7a6b6"
YOUR_APP_CLIENT_SECRET = "1034602c10984f658654b6241cd002db"
YOUR_APP_REDIRECT_URI = "http://example.com"
#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_CLIENT_ID,
        client_secret=YOUR_APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

        # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)

    # Adding songs found into the new playlist
