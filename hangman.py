import random
import string

# Hangman ASCII art
hangman_graphics = [
    '''
    +---+
        |
        |
        |
       ===
    ''',
    '''
    +---+
    O   |
        |
        |
       ===
    ''',
    '''
    +---+
    O   |
    |   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\\  |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\\  |
   /    |
       ===
    ''',
    '''
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
    '''
]

# Word categories
word_categories = {
    'animals': ['lion', 'elephant', 'giraffe', 'monkey', 'zebra'],
    'countries': ['india', 'brazil', 'canada', 'australia', 'japan'],
    'movies': ['inception', 'avatar', 'titanic', 'interstellar', 'jaws']
}

# Function to choose a random word from a category
def choose_word(category):
    return random.choice(word_categories[category])

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to play Hangman
def play_hangman():
    print("Welcome to Hangman!")

    # Choose word category
    category = input("Choose a word category (animals, countries, movies): ").lower()
    if category not in word_categories:
        print("Invalid category. Defaulting to 'animals'.")
        category = 'animals'

    # Choose difficulty level
    difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
    if difficulty == 'easy':
        max_attempts = 10
    elif difficulty == 'medium':
        max_attempts = 8
    elif difficulty == 'hard':
        max_attempts = 6
    else:
        print("Invalid difficulty level. Defaulting to 'medium'.")
        max_attempts = 8

    # Choose a random word
    secret_word = choose_word(category)
    guessed_letters = set()
    incorrect_attempts = 0

    while incorrect_attempts < max_attempts:
        print(hangman_graphics[incorrect_attempts])
        print("Word:", display_word(secret_word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            print("Incorrect guess.")
            incorrect_attempts += 1
        else:
            print("Correct guess!")

        if set(secret_word) <= guessed_letters:
            print("Congratulations! You guessed the word:", secret_word)
            break

    else:
        print(hangman_graphics[incorrect_attempts])
        print("Sorry, you ran out of attempts. The word was:", secret_word)

# Main game loop
play_hangman()
