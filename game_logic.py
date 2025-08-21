import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += '_'
    print(f"Word: {display_word}\n")


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print('"You already guessed that letter!"')
            continue
        guessed_letters.append(guess)
        # Check if guess is wrong
        if guess not in secret_word:
            mistakes += 1
        #check for game over
        if mistakes == len(STAGES) - 1:
            print(f"Game Over!The word was: {secret_word}")
            break
        # check for win
        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 you saved the snowman! congrats 🎊")
            break