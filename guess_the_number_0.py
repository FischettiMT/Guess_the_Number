import random
import os

os.system("cls")

guesses_taken = 0
guess = "?"

my_name = input("Hello! What is your name? ")

number = random.randint(1, 1000)

while guess != number:
    guesses_taken += 1
    guess = int(input(f"{my_name}, make guess #{guesses_taken}: "))

    if guess > number:
        print("your guess was too high!")

    if guess < number:
        print("your guess was too low!")

print(f"you guessed the number in #{guesses_taken} guesses! 😊😊")
print()
