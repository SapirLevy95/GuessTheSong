import random


class Artist:
    def __init__(self, artist):
        self.artist = artist
        self.random_numbers_list = random.sample(range(0, 10), 10)

    def remove_index_from_list(self, index):
        self.random_numbers_list.remove(index)
