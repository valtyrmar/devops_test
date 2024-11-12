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

def display_word(guessed_word):
    return ''.join(guessed_word)

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input, please enter only one letter.")

#play the game
def play_game():
    word = select_random_word()
    game = start_game(word)

    print("let's play hangman!")


play_game()