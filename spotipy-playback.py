import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from pprint import pprint
import time


scope = "user-read-playback-state,user-modify-playback-state"
username = 'advait.deshpande'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id='86ca0308b7d64ab89bc5e971936c3cd1',
                           client_secret='0c8db1e0081340f3882980e400d4b844',
                           redirect_uri='https://google.com/')

sp = spotipy.Spotify(auth=token)

# sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(username=username,redirect_uri="https://google.com/",client_id='86ca0308b7d64ab89bc5e971936c3cd1',client_secret='0c8db1e0081340f3882980e400d4b844',scope=scope))
# https://open.spotify.com/user/advait.deshpande?si=ifdhivgYQZ-5O4bAP93DEQ
# Shows playing devices
res = sp.devices()
pprint(res)
print(res['devices'][0]['id'])

# store first device id
device_id = res['devices'][0]['id']


# get current playing track

def track_details():
    cur2 = sp.currently_playing()
    cur_track_uri = cur2["item"]["uri"]
    # print(cur2["item"].keys())
    cur_track_name = cur2["item"]["name"]
    return cur_track_name

# go to next(1)/previous(2) track

def skip_track(n):
    if n == 1:
        sp.next_track(device_id)
    else:
        sp.previous_track(device_id)

# play/pause boolean
def play_pause(n):
    if n == 1:
        sp.start_playback(device_id)
    else:
        sp.pause_playback(device_id)


# while loop listens for user input
while True:
    user_control = input("select action (>, ||, f, b): ").lower()
    if user_control == '>':
        print('now playing: ' + track_details())
        try:
            play_pause(1)
        except Exception:
            continue
    elif user_control == '||':
        print('paused')
        play_pause(0)
        continue
    elif user_control == 'f':
        skip_track(1)
        time.sleep(0.5)
        print('skipped forward to: ' + track_details())
        continue
    elif user_control == 'b':
        skip_track(0)
        time.sleep(0.5)
        print('skipped back to: ' + track_details())
        continue
