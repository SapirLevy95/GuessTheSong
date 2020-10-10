import random
import utitilies

# In case this is const (configuration) for the system the variable name should be in UPPER CASE.
# Why this is a dict and not array? anyway all the values get 0. 
artists_dict = {"Evanescence": 0, "Carrie Underwood": 0, "Daughtry": 0, "Nightwish": 0}

score = 0
for random_song in range(10):
    random_artist = random.choice(list(artists_dict.keys()))
#     the "game" contains 10 rounds, so try to think about better naming for "start_the_game"
    score += utitilies.start_the_game(random_artist, artists_dict[random_artist])
#     Why do you count the number of songs that were played per artist? 
    artists_dict[random_artist] += 1
    print(artists_dict)
    print(f'current score = {score}\n')
