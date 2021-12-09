"""This module has the guess game for both user and the computer"""
from random import randint


def user_guess(x):
    """This function gets a random int from the module random
       it then takes input from the user to see if they got the correct number.
       it will exit once this happens"""
    guess = 0
    number = randint(1, highest_number)
    while guess is not number:
        guess = int(input(f"Guess a number between 1 and {x} and I will tell you if you are correct: "))
        if guess > number:
            print("You are too far from mine!")
        if guess < number:
            print("You are too low from mine!")
    print(f"You are a wizard of guesses. The number is indeed {number}")


def computer_guess(x):
    """This function is meant to make the computer guess if the random number
       is the same as the one guessed by user"""

    print(f"think of a number between {1} and {highest_number} and don't tell me")
    highest = x
    lowest = 1
    ans = ''
    while ans != "C":
        if lowest != highest:
            random_number = randint(lowest, highest)
        else:
            random_number = lowest
        ans = input(f"is {random_number} too high?")
        if ans == "Yes":
            highest = random_number - 1
        elif ans == "No":
            lowest = random_number + 1
    print("I am also a good guesser!!!")


highest_number = int(input("Enter the highest number you want to guess to: "))
# user_guess(highest_number)
computer_guess(highest_number)
