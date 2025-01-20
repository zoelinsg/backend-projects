from flask_restful import Resource
from flask import request
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os

class MusicRecommendation(Resource):
    def __init__(self):
        # 使用 Spotify API 認證
        client_credentials_manager = SpotifyClientCredentials(
            client_id=os.getenv('SPOTIPY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')
        )
        self.sp = Spotify(client_credentials_manager=client_credentials_manager)

    def get(self):
        genre = request.args.get('genre')
        # 搜尋符合類型的音樂
        results = self.sp.search(q=f'genre:{genre}', type='track', limit=5)
        tracks = [
            {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "url": track['external_urls']['spotify']
            }
            for track in results['tracks']['items']
        ]
        return {"genre": genre, "recommendations": tracks}