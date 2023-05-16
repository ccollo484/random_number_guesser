#Number Guessing Game

import random

python_number = random.randint(1, 100)

while True:
    print("What number between 1 and 100 is Python thinking of?")
    user_input = input()
    user_guess = int(user_input)

    if user_guess < python_number:
        print("Your guess is lower than Python's number!")

    elif user_guess > python_number:
        print("You guess is higher than pythons number")
    
    elif user_guess == python_number:
        print(f"Well done! Python's number was {python_number}.")
    break