from difflib import SequenceMatcher
import datetime
from Song import Song


# What is artist_value? 
def start_the_game(artist_name, artist_value):
    score = 0
    song = Song(artist_name, artist_value)
    print(song.song_name)
    song.media.play()
    #start_the_run_time and end_the_run_time sounds like an action (=function names) more then a noun, better naming might be start_time / runing_start_time 
    start_the_run_time = datetime.datetime.now()
    guessed_song = str(input("what's your guess? press 0 if you don't know")).lower()
    end_the_run_time = datetime.datetime.now()
    seconds_passed = (end_the_run_time - start_the_run_time).total_seconds()
    # the name is good, you can make is shorter like "similarity_percentage" with adjective
    percentage_of_similarity = SequenceMatcher(a=guessed_song, b=song.song_name).ratio()
#     The outout might not metch the senario, in case th player doesn't know and enter '0' after 1sec he sees "time's up" message which incorrect. 
    if guessed_song == '0':
        print("time's up")
# Dont use magic numbers, put them as consts on the top of the file. 
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
