'''
This is the main script to execute to run the game.

'''
from utils import game

if __name__ == "__main__":
    game = game.Hangman()
    game.start_game()

