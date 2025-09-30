from random import randint
from art import logo

HARD_LEVEL_ATTEMPTS = 10
EASY_LEVEL_ATTEMPTS = 5

# Function to check users guess with the answer
def check_answer(user_guess, actual_answer, turns):
    """Checks the guess against the answer, returns the number of turns left"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

# Function to set difficulty
def set_difficulty():
    level = input("Choose difficulty level. Type 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

# Function to play the game
def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}.")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get the answer wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts at guessing the number.")
        # Let the user pick a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce it by 1 if they are wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        elif guess != answer:
            print("Guess again.")

game()


