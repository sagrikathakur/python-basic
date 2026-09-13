# Number Guessing Game for Beginners
# Learning Concepts: The 'random' module, while loops, comparison (<, >, ==)

import random

print("=== NUMBER GUESSING GAME ===")
print("I am thinking of a number between 1 and 20.")

# Generate a random secret number
secret_number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("\nTake a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid whole number!")
