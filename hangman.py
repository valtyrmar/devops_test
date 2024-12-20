"""
This is a hangman game developed for entertainment purposes :)
Author: Valtýr Már Michaelsson
"""


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

#update based on a player's guess
def update_game_status(game_status, guess):
    if guess in game_status['guessed_letters']:
        print(f"The letter '{guess}' has already been guessed.")
        return

    game_status['guessed_letters'].add(guess)

    if guess in game_status['word']:
        for i, char in enumerate(game_status['word']):
            if char == guess:
                game_status['guessed_word'][i] = guess
        print("Correct!")
    else:
        game_status['attempts'] -= 1
        print("Incorrect :(")

#check if the game has been won
def game_won(game_status):
    return '_' not in game_status['guessed_word']

#check if the game has been lost
def game_lost(game_status):
    return game_status['attempts'] <= 0

#play the game
def play_game():
    word = select_random_word()
    game_status = start_game(word)

    print("let's play hangman!")

    while not game_won(game_status) and not game_lost(game_status):
        print("\nWord:", display_word(game_status['guessed_word']))
        print("Attempts left:", game_status['attempts'])
        guess = get_guess()
        update_game_status(game_status, guess)

    if game_won(game_status):
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over. The word was:", word)

play_game()