"""
This is a hangman game developed for entertainment purposes :)
Author: Valtýr Már Michaelsson
"""

import random
import getpass

#select a word for the other player to guess
#getpass hides the word from the guesser
def select_random_word():
    word = getpass.getpass("Enter a word: ").lower()
    return word

#start the game
def start_game(word):
    return {'word': word,
            'guessed_word': ['_']*len(word),
            'guessed_letters': set(),
            'attempts': 8
            }

#play the game
def play_game():
    word = select_random_word()
    game = start_game(word)

    print("let's play hangman!")