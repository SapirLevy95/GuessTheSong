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
        self.song_name = self.get_song_name()
        self.media = self.get_media()

#     For each song the ctor call this function twice, think on a way to call this only once.
# in most of the languages you have private and public fields, but in python you dont have, so the developer started a convention that each field/function that is private should start with _, for example 
# _get_song_url. please update all your project depend on this convention (you can rename stuff by Shift + F6/F2 )
    def get_song_url(self):
        query_string = urllib.parse.urlencode({"search_query": self.artist})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        url = "http://www.youtube.com/watch?v={}".format(search_results[self.artist_value])
        return url

    def get_song_name(self):
        url = self.get_song_url()
        request = requests.get(url)
        s = BeautifulSoup(request.text, "html.parser")
        song_name = s.find("title").text.replace("\n", "").lower()
# really long line, hard to read, try split it into more readable lines. 
        song_name = re.sub(r'(youtube)', '', re.sub(r'\(.*\)', '', song_name)) \
            .replace('-', '').replace(self.artist.lower(), "").strip().lower()
        return song_name

    def get_media(self):
        url = self.get_song_url()
        video = pafy.new(url)
        best = video.getbestaudio()
        media = vlc.MediaPlayer(best.url)
        return media
