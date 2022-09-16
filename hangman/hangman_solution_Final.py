'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from ast import While
from dataclasses import replace
from http.client import OK
import random
from subprocess import call

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
    '''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # DONE -- 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = list(random.choice(word_list))

        self.word_guessed = []
        while len(self.word_guessed) != len(self.word):
            self.word_guessed.append('_')
        else:
            print(self.word_guessed)

        self.list_letters = []

        print(f'The mystery word has {len(self.word)} characters')

        pass



#------ Extra function, to replace correctly guessed letter if it appears in the word more than once
    def find_indices(self, list_to_check, letter_to_check, blank_list):
        index_list = []
        #print(self.word_guessed)
        for idx, value in enumerate(self.word):
            if value == letter_to_check:
                index_list.append(idx)
                blank_list[idx] = letter_to_check
                #print(blank_list)
        return #index_list, list_to_check



    def check_letter(self, letter): # -> None:     ------     Removed '-> None"
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3.1 : Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # DONE -- TODO 3.2 : If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3.3 : If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # DONE -- TODO 3.4 : If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class

        # Letter IS in the word
        if self.letter in self.word:
                print('Nice, this letter is in the word!')
                self.list_letters.append(self.letter)
                print(f'Letters guessed : {self.list_letters}')
                #print('count : ', self.word.count(self.letter))

                # ------------
                self.letter_index = self.word.index(self.letter)
                #print('index : ', self.letter_index)

                # ----- USING NEW FUNCTION 'FIND_INDICES' --------
                print(Hangman.find_indices(self, self.word, self.letter, self.word_guessed))
                
                
                # TODO 3.2 --- DONE
                self.word_guessed[self.letter_index] = self.letter
                print(self.word_guessed)



        # Letter NOT in the word
        else:
                self.list_letters.append(self.letter)
                print(self.list_letters)
                print("Damn, this letter is NOT in the word!")
                print(f'Letters guessed : {self.list_letters}')

                # TODO 3.4 --- DONE
                self.num_lives = self.num_lives -1
                print(f'You have {self.num_lives} lives left!')

        pass


    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            self.letter = input("Enter a letter : ")
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

                
            
                

        # DONE -- TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # DONE -- TODO 1: Assign the letter to a variable called `letter`
        # DONE -- TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # DONE -- TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # DONE -- TODO 3: If the letter is valid, call the check_letter method
            pass
        

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # DONE -- TODO 1: To test this task, you can call the ask_letter method
    game.ask_letter()
    # DONE -- TODO 2: To test this task, upon initialization, two messages should be printed 
    # DONE -- TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    # CODE FOR TODO 4 BELOW ------------------------- 

    # if self.num_lives <= 0:
    #        print(f"You ran out of lives. The word was {self.word}")
    #        break
    # else:
    #   pass

    pass

if __name__ == '__main__':
    word_list = ['apple'] # 'pear', 'banana', 'orange', 'strawberry', 'watermelon'
    play_game(word_list)
# %%
