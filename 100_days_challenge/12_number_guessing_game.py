import random
from additional_files.art_12 import logo


def difficulty():
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficult == 'easy':
        return 10
    else:
        return 5


def check_guess(attempts, guess, number):
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        return number


def number_guessing():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 101)
    attempt = difficulty()
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt = check_guess(attempt, guess, number)
        if attempt == number:
            return f"You got it! The answer was {number}."
    return "You've run out of guesses, you lose."


print(number_guessing())
