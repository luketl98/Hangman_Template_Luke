from ast import While
from dataclasses import replace
from http.client import OK
import random
from subprocess import call
import sys

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    DONE -- word: str
        The word to be guessed picked randomly from the word_list
    NOT DONE PROPERLY -- word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not yet been guessed yet
    DONE -- num_lives: int
        The number of lives the player has
    DONE -- list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    find_indicies()
    '''
    
    def __init__(self, word_list, num_lives=5):

        # List of words to be used in the game
        self.word_list = word_list 
        # Number of lives the player has
        self.num_lives = num_lives
        # Picks a word at random from the word list to be used as the mystery word
        self.word = list(random.choice(word_list))
        print("\n")
        # Prints the number of letters in the mystery word
        print(f'The mystery word has {len(self.word)} characters')

        # Converts the mystery word into a list of "empty" spaces with 
        # the same number of characters as the word itself (i.e apple = '_''_''_''_''_' )
        self.word_guessed = []
        while len(self.word_guessed) != len(self.word):
            self.word_guessed.append('_')
        else:
            print(self.word_guessed)

        # Creates the list for guessed letters to be appended to
        self.list_letters = []

        pass



    # A function used to replace a correctly guessed letter,
    # if it appears in the mystery word more than once

    def find_indices(self, list_to_check, letter_to_check, blank_list):

        for idx, value in enumerate(self.word):
            if value == letter_to_check:
                blank_list[idx] = letter_to_check
        return 




    def check_letter(self, letter) -> None:    
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
       
        # Visualised stages of hangman
        visual_1 = """
                    
                     




                    =========

                    """
        visual_2 = """
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                    =========
                    """
        visual_3 = """
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    =========
                    """
        visual_4 = """
                    +---+
                    |   |
                    O   |
                   /|\  |
                     \  |
                        |
                    =========
                    """
        visual_5 = """
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                    =========
                    """

        
        # Rejoins the mystery word into a single string for improved readability
        joined_list = ' '.join(self.word)

        # If letter IS in the word
        if self.letter in self.word:

            # Adds the guessed letter to the list of guessed letters
            self.list_letters.append(self.letter)

            # finds the index of the guessed letter in the mystery word
            self.letter_index = self.word.index(self.letter)

            # Calls the find_indicies function
            Hangman.find_indices(self, self.word, self.letter, self.word_guessed)
            
            # Replaces the guessed letter with the 
            self.word_guessed[self.letter_index] = self.letter

            # If the user guesses all letters correctly and wins the game
            if self.word_guessed.count('_') == 0:
                print("Congratulations, you won!")
                print('\n')

                print(f'The word was {joined_list}')
                print('\n')

                # Asks the user if they want to play again if they won,
                # exits if no, reruns the program if yes
                if input("Do you want to play again (y/n)") == 'n':
                    sys.exit()
                else:
                    print("\n")
                    print("You didn't say no, so here we go again!")
                    game2 = Hangman(word_list, num_lives=5)
                    game2.ask_letter()
            else:
                # If the letter is correct and the user still has more than 1 life left
                print('Nice, this letter is in the word!')
                print(f'Letters guessed : {self.list_letters}')
                print(self.word_guessed)


        # If letter is NOT in the word
        else:
                # Tells player the letter is incorrect and appends it to list_letters
                self.list_letters.append(self.letter)
                print("Damn, this letter is NOT in the word!")

                # Removes a life
                self.num_lives = self.num_lives-1

                # Returns the remaining number of lives and letters guessed,
                # except if the player has 0 lives left
                if self.num_lives == 0:
                    pass
                else:
                    print(f'Letters guessed : {self.list_letters}')
                    print(f'You have {self.num_lives} lives left!')
                    print(self.word_guessed)

                # Prints the hangman visuals 
                if self.num_lives == 4:
                    print(visual_1)
                elif self.num_lives == 3:
                    print(visual_2)
                elif self.num_lives == 2:
                    print(visual_3)
                elif self.num_lives == 1:
                    print(visual_4)
                else:
                    pass
                

                # Tells player they failed, reveals the word and prints the final visual
                if self.num_lives == 0:
                    print(f'You ran out of lives. The word was {joined_list}')
                    print(visual_5)
                else:
                    pass
        
        pass


    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # Checks that the user still has lives remaining, 
        # then proceeds with the the ask_letter function
        while self.num_lives != 0:
            print("\n")
            # Asks the user to input a letter
            self.letter = input("Enter a letter : ")
            print('\n')
            # Converts the letter to lower case to allow uppercase letters to be used in the game
            self.letter = self.letter.lower()
            # Checks that letter is an alphabetical character
            if self.letter.isalpha() == False:
                print("Please, enter an alphabetical character")

            # Checks that user inputs just one letter
            elif len(self.letter) != 1 :
                print("Please, enter just one character")

            # Checks if letter has already been tried
            elif self.list_letters.count(self.letter) == True:
                print(f'{self.letter} was already tried')

            # Calls check_letter method
            else:
                Hangman.check_letter(self, self.letter)

                # Asks the user if they want to play again if they failed,
                # exits if no, reruns the program if yes
                if input("Do you want to play again (y/n)") == 'n':
                    sys.exit()
                else:
                    print("\n")
                    print("You didn't say no, so here we go again!")
                    game2 = Hangman(word_list, num_lives=5)
                    game2.ask_letter()

            pass
        

def play_game(word_list):
    # Calls ask_letter function
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    pass

if __name__ == '__main__':
    # A list for words to be selected from for the game
    word_list = ['apple', 'pear', 'banana', 'orange', 'strawberry', 'watermelon'] 
    # Calls play_game function and begins the program
    play_game(word_list)


# %%
