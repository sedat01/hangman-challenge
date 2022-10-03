import string
from typing import List
from random import choice

class Hangman:
    '''
    Main class of the game that contains all the necessary attributes and methods
    .play() method serves as the main engine.
    .game_over() handles the loss condition
    .well_played() handles the win condition
    .start_game() starts the game and checks for win or loss
    '''
    def __init__(self) -> None:
        '''
        Initialization includes attributes and also chooses a word to be guessed.
        .possible_words is a list with words to choose from. New words can be added to this list
        to expand the library of word the game can be played with
        .word_to_find is selected from .possible_words list at random in the start of the game
        .well_guessed_letters is a list which stores the good guesses. It is initialized in the
        beginning with "_" (underscore) for every character in the word to find
        .bad_guessed_letters stores the bad guesses 
        .turn_count stores the number of turns passed
        .error_count stores to number of bad guesses
        .lives stores the number of lives. This can be modified to change the initial number of lives.
        Default value is 5
        '''
        with open("./utils/word_list.txt","r",encoding="utf-8") as word_list:
            word_list.seek(0)
            words = word_list.read().split()
            self.possible_words: List[str] = words
        self.word_to_find: List[str] = [*choice(self.possible_words)]
        self.well_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        self.bad_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.lives: int = 5
        print("Welcome to Hangman")
        print(f"Word to guess :{self.well_guessed_letters}")
        
        
        
    def play(self):
        '''
        Main game engine. It takes input from the player and first checks if it as a letter and
        if it is only a single character. Then the function proceeds to check if the letter is 
        in the word to find and if that condition is True then it finds if the letter is
        used 1 or more times in the word the find and modifies .well_guessed_letters to represent 
        the result after the guess.
        If the guess is bad the function modifies bad_guessed_letters, error_count and lives
        '''
        while True:
            letter: str = input("Please enter a letter ")
            letter = letter.lower()
            if len(letter) == 1:
                if letter in string.ascii_letters:
                    break
                print("Please enter letter ")
            else:
                print("Please enter only one letter ")
                
        letter_in_word: List[int] = []
        if letter in self.word_to_find:
            for char in range(len(self.word_to_find)):
                if self.word_to_find[char] == letter:
                    letter_in_word.append(char)
        self.turn_count += 1
        if len(letter_in_word) > 0:
            for i in range(len(letter_in_word)):
                self.well_guessed_letters[letter_in_word[i]] = letter
        else:
            self.bad_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
        
        
    def game_over(self):
        '''
        This function is called when the game ends in loss for the Player.
        It prints "Game over..." message
        '''
        print("Game over...")
        
    def well_played(self):
        '''
        This function is called when the game ends in win for the Player.
        It prints the guessed word, number of turns and number of errors.
        '''
        guessed_word: str = ""
        guessed_word = guessed_word.join(self.word_to_find)
        print(f"You found the word: {guessed_word} in {self.turn_count} turns with {self.error_count} errors!")
        
    def start_game(self):
        '''
        This function starts the game and checks for win and loss conditions and
        call the coresponding functions.
        game_over (type Boolean) variable is used as a condtion for the while loop.
        it is set to True if a win or loss condition is fulfilled. It is set to False
        in the start of the game and changed to True if Player runs out of lives or guesses the 
        word correctly
        '''
        print("Game starting ")
        game_over: bool = False
        while not game_over:
            self.play()
            print(f"Guessed letter:{self.well_guessed_letters}")
            print(f"Bad guesses: {self.bad_guessed_letters}")
            print(f"Lives remaining: {self.lives}")
            print(f"Errors made: {self.error_count}")
            print(f"Turns played: {self.turn_count}")
            
            if self.lives == 0:
                game_over = True
                self.game_over()
            
            if self.well_guessed_letters == self.word_to_find:
                game_over = True
                self.well_played()