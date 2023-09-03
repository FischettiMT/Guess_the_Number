import random
import os, time
from Maxs_Module import *

os.system("cls")

number_of_guesses = 0
guess = "?"

my_name = input("Hello! What is your name? ")
max_number = int(input("What maximum number would you like? "))
min_number = 1
print()

secret_number = random.randint(min_number, max_number)

while guess != secret_number:
    os.system("cls")
    print(
        f"Well, {my_name}, I am thinking of a number between {min_number} and {max_number}."
    )

    number_of_guesses += 1
    guess = int(input(f"{my_name}, make guess #{number_of_guesses}: "))

    if guess > secret_number:
        print(f"{RED_type}Your guess was too high!{DEFAULT_type}")
        if guess < max_number:
            max_number = guess

    if guess < secret_number:
        print(f"{BLUE_type}Your guess was too low!{DEFAULT_type}")
        if guess > min_number:
            min_number = guess

    time.sleep(1)

print(
    f"{GREEN_type}you guessed the number in #{number_of_guesses} guesses! 😊😊{DEFAULT_type}"
)
print()
