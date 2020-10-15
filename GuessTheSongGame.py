import random
from difflib import SequenceMatcher
import datetime
from Song import Song

from Artist import Artist

MAX_TIME = 60
MIN_SIMILARITY_PERCENTAGE = 0.9


class GuessTheSongGame:
    def __init__(self):
        self.artists_list = [Artist("Evanescence"), Artist("Carrie Underwood"), Artist("Daughtry"), Artist("Nightwish")]
        self.score = 0

    def start_game(self):
        for random_song in range(10):
            random_artist = random.choice(list(self.artists_list))
            artist_name = random_artist.artist
            random_index_song_artist = random.choice(random_artist.random_numbers_list)
            self.score += self._start_a_round(artist_name, random_index_song_artist)
            random_artist.remove_index_from_list(random_index_song_artist)
            print(f'current score = {self.score}\n')

    @staticmethod
    def _start_a_round(artist_name, song_index_in_youtube):
        score = 0
        song = Song(artist_name, song_index_in_youtube)
        print(song.song_name)
        song.media.play()
        running_start_time = datetime.datetime.now()
        guessed_song = str(input("what's your guess? press 0 if you don't know")).lower()
        running_end_time = datetime.datetime.now()
        seconds_passed = (running_end_time - running_start_time).total_seconds()
        similarity_percentage = SequenceMatcher(a=guessed_song, b=song.song_name).ratio()
        if guessed_song == '0':
            print("There isn't a guess. No points for you")
        elif similarity_percentage > MIN_SIMILARITY_PERCENTAGE:
            if seconds_passed < MAX_TIME:
                score = round((-1 / 3 * seconds_passed) + 60)
                print(f"Succeeded. you've got {score} points")
            else:
                print("time's up")
        else:
            print("failed. No points for you")
        song.media.stop()
        return score
