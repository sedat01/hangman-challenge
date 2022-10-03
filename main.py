'''
This is the main script to execute to run the game.

'''
'''This is used to prevent generation of pychache files'''
import sys
sys.dont_write_bytecode = True 
'''Importing main game function'''
from utils import game

if __name__ == "__main__":
    game = game.Hangman()
    game.start_game()
