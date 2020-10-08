from difflib import SequenceMatcher
import datetime
from Song import Song


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
            score = round((-1 / 3 * seconds_passed) + 60)
            print("Succeeded")
        else:
            print("time's up")
    else:
        print("failed")
    song.media.stop()
    return score
