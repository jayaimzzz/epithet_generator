import json
import os
import random

class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!

    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)

class EpithetGenerator:
    def __init__(self, path=os.path.join("resources","data.json")):
        self.set_vocab(path)

    def set_vocab(self, path):
        self.vocab = Vocabulary.read_json(path)
    
    def get_random_words(self):
        random_word_1 = random.choice(self.vocab.get('Column 1'))
        random_word_2 = random.choice(self.vocab.get('Column 2'))
        random_word_3 = random.choice(self.vocab.get('Column 3'))
        return (f'{random_word_1} {random_word_2} {random_word_3}')

    def get_epithets(self, qty=1):
        result = [''] * qty
        return [self.get_random_words() for item in result]