# Hangman_luketl98
### Hangman Game in Python

This is a simple command-line Hangman game written in Python. The game selects a random word from a list of fruits and prompts the player to guess the word letter by letter. Each incorrect guess results in a part of the hangman being drawn. The game ends when the player guesses the word correctly or the hangman is completely drawn.


**Getting Started**

To run this game, simply navigate to the directory containing the hangman.py file and type the following command in your terminal:

`python hangman.py`


**Game Play**

At the start of the game, the player is shown a series of underscores corresponding to the number of letters in the word to be guessed.

The player is prompted to guess a letter in the word.

If the letter is in the word, the positions of the letter in the word are revealed. If the letter is not in the word, a part of the hangman is drawn.

The game continues with the player guessing letters until they either correctly guess the word or the hangman is fully drawn, indicating that the player has run out of guesses.

After the game ends, the player is given an option to play again.


**Code Overview**

Hangman class: Manages the state of the game.

print_nl function: Prints its arguments followed by two newline characters.

main function: Starts the game with a list of possible words.

The Hangman class contains several methods that manage the gameplay:

`__init__`: Initializes a new game with a random word from the provided list and sets the number of lives.

`find_indices`: Finds the indices of a given letter in the word.

`check_letter`: Checks if a guessed letter is in the word and updates the game state.

`ask_letter`: Prompts the player to guess a letter and checks its validity.

`play_again`: Asks the player if they want to start a new game after the current game ends.


**Contributions**

Feel free to fork the project and make your own improvements or additions to the game.

Enjoy the game!
