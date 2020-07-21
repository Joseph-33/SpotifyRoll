import spotipy.util as util
import spotipy
import yaml
from SpModules import get_top_songs_for_artist, playlist_id, convert_to_uri, split_artist, user_playlist_tracks_full, uri_from_playlist

stream = open("config.yaml") # Opens the config Path
user_config = yaml.safe_load(stream) # Safe Loads using yaml
user_id = user_config['username'] # Spotify Username
personal_playlist_name = user_config["personal_playlist_name"] # The name of the users personal spotify playlist to overwrite and save the songs to
artist_name = user_config["artist"]
track_name = user_config["track"]


if not track_name:
    track_name = input("Input Track Name\n")


if not artist_name:
    artist_name = input("Input Artist Name\n")



scope='playlist-modify-private,playlist-read-private,playlist-read-collaborative'
token = util.prompt_for_user_token(user_config['username'], scope=scope, client_id=user_config['client_id'], client_secret=user_config['client_secret'], redirect_uri=user_config['redirect_uri']) # Generates a token
sp = spotipy.Spotify(auth=token) # Create a Spotipy Instance

my_playlist_id = playlist_id(personal_playlist_name,sp)  # Gets the playlist id from the name

artist_songs = [artist_name,track_name]

artist_results = get_top_songs_for_artist([artist_songs],sp) # Obtain spotipy searches from the artist_song list
target_uri = convert_to_uri(artist_results)[0] # Obtain song uri's from the spotipy searches
user_playlist_tracks = user_playlist_tracks_full(sp,user_id,my_playlist_id)


my_playlist_tracks = user_playlist_tracks_full(sp,user_id,my_playlist_id)
uri_list = uri_from_playlist(sp,my_playlist_tracks)

target_index = None
for uri_index in range(len(uri_list)):
    if target_uri == uri_list[uri_index]:
        target_index = uri_index
        break

if target_index == None:
    raise Exception("Song not found in playlist")
print("Found song in playlist")
new_uri_list = uri_list[target_index:] + uri_list[:target_index]

sp.user_playlist_replace_tracks(user_id,my_playlist_id,[]) # Clears the playlist

chunk_size = 99 # Spotify can only accept 100 tracks
for i in range(0, len(new_uri_list), chunk_size):
    print("Adding chunk",int(i/chunk_size)+1)
    chunk = new_uri_list[i:i+chunk_size] # Designate the chunk
    sp.user_playlist_add_tracks(user_id,my_playlist_id,chunk,position = i) # Add the uri tracks to the spotipy playlist
