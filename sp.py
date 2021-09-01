import urwid 
import os
import sys
import secrets
import requests
import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def current_track(sp):
    track = sp.current_user_playing_track()
    return(track['item']['name'] + " - " + track['item']['artists'][0]['name'])

def main():
    # bad idea to given all scopes so fix this later
    scope = "playlist-modify-private, playlist-read-private, user-read-private, user-read-playback-state, user-library-modify, user-read-playback-position, app-remote-control, user-read-recently-played, user-modify-playback-state, user-read-email, user-follow-modify, playlist-modify-public, user-follow-read, user-read-currently-playing, playlist-read-collaborative, user-library-read, streaming, user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    print(current_track(sp))

if __name__ == "__main__":
    main()
