import random
from curses.ascii import isalpha

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects and returns a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the game:
    - Snowman ASCII art based on mistakes
    - The secret word with guessed letters revealed
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += '_'
    print(f"Word: {display_word}\n")


def play_game():
    """
    Runs the main Snowman game loop. Handles:
    - Input validation
    - Tracking guessed letters
    - Win/loss detection
    - Replay option for multiple rounds
    """
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    is_game_ends = False
    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print('Please enter exactly one letter!')
            continue
        elif not guess.isalpha():
            print('Please enter a letter (a-z)')
            continue
        if guess in guessed_letters:
            print('You already guessed that letter!')
            continue

        guessed_letters.append(guess)
        # Check if guess is wrong
        if guess not in secret_word:
            mistakes += 1
        else:
            print(f"Good job! '{guess}' is in the word.")

        #check for game over
        if mistakes == len(STAGES) - 1:
            print(f"Game Over! The word was: {secret_word}")
            is_game_ends = True

        # check for win
        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 you saved the snowman! congrats 🎊")
            is_game_ends = True

        if is_game_ends:
            wants_to_play_prompt = input('Do you want to play another round ? (y/n)').lower().strip()
            if wants_to_play_prompt == 'y':
                mistakes = 0
                guessed_letters = []
                secret_word = get_random_word()
                is_game_ends = False
                continue
            else:
                break
