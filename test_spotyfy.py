import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()
client_id = os.getenv('client_id')
client_secret =os.getenv('client_secret')
ccm = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)
print(client_id, client_secret)
def search_sound(song_name, artist_name):
    if not song_name and not artist_name:
        print("曲名またはアーティスト名を指定してください。")
        return [{"error": "曲名またはアーティスト名を指定してください。"}]

    if not song_name:
        query = f"artist:{artist_name}"
    elif not artist_name:
        query = f"track:{song_name}"
    else:
        query = f"track:{song_name} artist:{artist_name}"

    results = spotify.search(q=query, limit=1, type="track", market="JP", offset=0)
    song_list = []
    for track in results["tracks"]["items"]:
        song_name = track["name"]  # 曲名
        artist_name = ", ".join([artist["name"] for artist in track["artists"]])  # アーティスト名をリストから取得してカンマで連結
        album_name = track["album"]["name"]  # アルバム名
        release_date = track["album"]["release_date"]  # リリース日
        popularity = track["popularity"]  # 人気度
        duration_ms = track["duration_ms"]  # 曲の長さ(ms)
        track_id = track["id"]  # トラックID
        preview_url = track["preview_url"]  # プレビューURL
        album_image = track["album"]["images"][0]["url"]  # アルバム画像URL
        print(f"曲名{song_name}, アーティスト{artist_name}, アルバム名{album_name}, リリース日{release_date}, 人気度{popularity}, 曲の長さ{duration_ms}, トラックID{track_id}, URL{preview_url}, アルバム画像{album_image}")
        song_list.append((song_name, artist_name, preview_url, album_image))
    return song_list

search_sound("ハッピーエンド", "back number")


