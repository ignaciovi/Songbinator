from flask import Flask, request
from flask import render_template
from random import shuffle
import spotipy.oauth2 as oauth2
import requests

def getSimilarArtists(artist_name):
    creds = oauth2.SpotifyClientCredentials(client_id="c2d07b756064444495ab44c7d14d4a81", client_secret="c6bae7d2398d4098b0d1435d7a7cf486")
    token = creds.get_access_token()

    spotify_id_request = requests.get(
        "https://api.spotify.com/v1/search?q={}&type=artist".format(artist_name),
        headers={"Authorization": "Bearer {}".format(token)}).json()

    artist_id = spotify_id_request["artists"]["items"][0]["id"]

    spotify_id_request = requests.get(
        "https://api.spotify.com/v1/artists/{}/related-artists".format(artist_id),
        headers={"Authorization": "Bearer {}".format(token)}).json()

    if spotify_id_request:
        related_artists = [{"name": artist["name"]} for artist in spotify_id_request["artists"]]
        related_artists.append({"name": artist_name})
        if (len(related_artists) > 5):
            shuffle(related_artists)
        related_artist_json = {"related_artists": related_artists[0:5]}

    return related_artist_json