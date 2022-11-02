import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# ------------------------------ PARAMETERS --------------------------------------#
URL = f"https://www.billboard.com/charts/hot-100/{date}"
REDIRECT_URL = "http://example.com"
CLIENT_ID = ""
CLIENT_SECRET = ""
# ---------------------------- AUTHENTICATION --------------------------------------#
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path='.cache'))
# --------------------------------------------------------------------------------#
user_id = sp.current_user()["id"]
song_names = ["The list of song", "titles from your", "web scrape"]

billboard_content = requests.get(URL).text
soup = BeautifulSoup(billboard_content, "html.parser")
titles = [title.getText().strip() for title in soup.select("li #title-of-a-story")]
song_uris = []

for title in titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
