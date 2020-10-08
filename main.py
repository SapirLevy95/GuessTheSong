import random
import utitilies

artists_dict = {"Evanescence": 0, "Carrie Underwood": 0, "Daughtry": 0, "Nightwish": 0}
score = 0
for random_song in range(10):
    random_artist = random.choice(list(artists_dict.keys()))
    score += utitilies.start_the_game(random_artist, artists_dict[random_artist])
    artists_dict[random_artist] += 1
    print(artists_dict)
    print(f'current score = {score}\n')
