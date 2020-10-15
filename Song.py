import pafy
import requests
import vlc
import urllib.request
import urllib.parse
import re
import urllib
from bs4 import BeautifulSoup


class Song:
    def __init__(self, artist, artist_value):
        self.artist = artist
        self.artist_value = artist_value
        self.url = self._get_song_url()
        self.song_name = self._get_song_name()
        self.media = self._get_media()

    def _get_song_url(self):
        query_string = urllib.parse.urlencode({"search_query": self.artist + " official music video"})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        url = "http://www.youtube.com/watch?v={}".format(search_results[self.artist_value])
        return url

    def _get_song_name(self):
        request = requests.get(self.url)
        s = BeautifulSoup(request.text, "html.parser")
        full_youtube_song_name = s.find("title").text.replace("\n", "").lower()
        print(full_youtube_song_name)
        print(self.artist + " official music video")
        song_artist_and_name = re.sub(r'(youtube)', '', re.sub(r'\(.*\)', '', full_youtube_song_name)) \
            .replace('-', '')
        song_name_only = song_artist_and_name.replace(self.artist.lower(), "").strip().lower()
        return song_name_only

    def _get_media(self):
        video = pafy.new(self.url)
        best = video.getbestaudio()
        media = vlc.MediaPlayer(best.url)
        return media
