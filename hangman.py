"""
This is a hangman game developed for entertainment purposes :)
Author: Valtýr Már Michaelsson
"""

import random
import getpass

def select_random_word():
    word = getpass.getpass("Enter a word: ").lower()
    return word