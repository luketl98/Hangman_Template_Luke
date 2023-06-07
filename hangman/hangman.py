import random
import sys

def print_nl(*args, **kwargs):
    """
    This function wraps around the print function, adding an extra newline at the end.
    """
    print(*args, **kwargs, end='\n\n')

class Hangman:
    """
    Hangman class for managing game state.
    """
    HANGMAN_VISUALS = [
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
         \  |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        =========
        """
    ]

    def __init__(self, word_list, num_lives=5):
        """
        Initialize hangman game with given word list and number of lives.
        """
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = list(random.choice(word_list))
        print("\n")
        print(f'The mystery word has {len(self.word)} characters')
        self.word_guessed = ['_'] * len(self.word)
        print_nl(self.word_guessed)
        self.list_letters = []

    def find_indices(self, list_to_check, letter_to_check, blank_list):
        """
        Find indices of a given letter in list and replace those indices in blank list.
        """
        for idx, value in enumerate(self.word):
            if value == letter_to_check:
                blank_list[idx] = letter_to_check

    def check_letter(self, letter):
        """
        Check if a given letter is in the word and update game state.
        """
        joined_list = ' '.join(self.word)
        if letter in self.word:
            self.list_letters.append(letter)
            self.find_indices(self.word, letter, self.word_guessed)
            if self.word_guessed.count('_') == 0:
                print_nl("Congratulations, you won!")
                self.play_again()
            else:
                print_nl(f'Good guess, the letter {letter} is in the word')
                print(f'Letters guessed : {self.list_letters}')
                print(' '.join(self.word_guessed))
        else:
            print_nl(f'Sorry, the letter {letter} is not in the word')
            self.num_lives -= 1
            print(self.HANGMAN_VISUALS[self.num_lives])
            self.list_letters.append(letter)
            print_nl(f'Letters guessed : {self.list_letters}')
            print(' '.join(self.word_guessed))
            if self.num_lives == 0:
                print("Game Over! You have run out of lives.")
                print(f'The word was: {joined_list}')
                self.play_again()

    def ask_letter(self):
        """
        Ask user for a letter and check if it is valid.
        """
        while self.num_lives > 0:
            print("\n")
            self.letter = input('Enter your guess: ')
            print("\n")
            if len(self.letter) != 1:
                print_nl('Please enter only one letter!')
                print_nl(f'Letters guessed : {self.list_letters}')
                print_nl(' '.join(self.word_guessed))
            elif self.letter in self.list_letters:
                print_nl("You've already guessed this letter!")
                print_nl(f'Letters guessed : {self.list_letters}')
                print_nl(' '.join(self.word_guessed))
            else:
                self.check_letter(self.letter)

    def play_again(self):
        """
        Ask user if they want to play again and either exit or start a new game.
        """
        if input("Do you want to play again (y/n)") == 'n':
            sys.exit()
        else:
            print("\n")
            print("Here we go again!")
            game = Hangman(self.word_list, num_lives=self.num_lives)
            game.ask_letter()


def main():
    """
    Main function to start the hangman game.
    """
    word_list = ['apple', 'banana', 'mango', 'cherry']
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()


if __name__ == "__main__":
    main()
