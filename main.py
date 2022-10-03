'''
This is the main script to execute to run the game.

'''
from utils import game

def main():
    game = game.Hangman()
    game.start_game()
    
if __name__ == 'main':
    main()
