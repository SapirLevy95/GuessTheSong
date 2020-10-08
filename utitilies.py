from _thread import interrupt_main
import pafy
import requests
import vlc
import urllib.request
import urllib.parse
import re
import urllib
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
import threading
import datetime


def raw_input_with_timeout(msg, timeout=10.0):
    timer = threading.Timer(timeout, interrupt_main)
    guessed_song = None
    try:
        timer.start()
        guessed_song = input(msg)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return guessed_song


class Song:
    def __init__(self, artist, artist_value):
        self.artist = artist
        self.artist_value = artist_value
        self.song_name = self.get_song_name()
        self.media = self.get_media()

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
        song_name = re.sub(r'(youtube)', '', re.sub(r'\(.*\)', '', song_name)) \
            .replace('-', '').replace(self.artist.lower(), "").strip().lower()
        return song_name

    def get_media(self):
        url = self.get_song_url()
        video = pafy.new(url)
        best = video.getbestaudio()
        media = vlc.MediaPlayer(best.url)
        return media


def start_the_game(artist_name, artist_value):
    score = 0
    song = Song(artist_name, artist_value)
    print(song.song_name)
    song.media.play()
    start_the_run_time = datetime.datetime.now()
    guessed_song = str(input("what's your guess? press 0 if you don't know")).lower()
    end_the_run_time = datetime.datetime.now()
    seconds_passed = (end_the_run_time - start_the_run_time).total_seconds()
    percentage_of_similarity = SequenceMatcher(a=guessed_song, b=song.song_name).ratio()

    if guessed_song == '0':
        print("time's up")
    elif percentage_of_similarity > 0.9:
        if seconds_passed < 60:
            score = (-1 / 3 * seconds_passed) + 60
            print("Succeeded")
        else:
            print("time's up")
    else:
        print("failed")
    song.media.stop()
    return score
