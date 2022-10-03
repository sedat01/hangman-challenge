import string
from typing import List
from random import choice

class Hangman:
    def __init__(self) -> None:
        self.possible_words: List[str] = ["becode", "learning", "mathematics", "sessions"]
        self.word_to_find: List[str] = []
        self.well_guessed_letters: List[str] = []
        self.bad_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.lives: int = 5
        self.word_to_find = [*choice(self.possible_words)]
        self.well_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        print("Welcome to Hangman")
        
        
        
    def play(self):
        while True:
            letter: str = input("Please enter a letter ")
            letter = letter.lower()
            if len(letter) == 1:
                if letter in string.ascii_letters:
                    break
                print("Please enter letter ")
            else:
                print("Please enter only one letter ")
                
        letter_in_word = []
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
        print("Game over...")
        
    def well_played(self):
        guessed_word = ""
        guessed_word = guessed_word.join(self.word_to_find)
        print(f"You found the word: {guessed_word} in {self.turn_count} turns with {self.error_count} errors!")
        
    def start_game(self):
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