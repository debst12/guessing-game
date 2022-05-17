"""A number-guessing game."""
# Put your code here


import random
name = input("Hello! What is your name? ")
print(f"{name}, I am thinking of a number between 1 and 100")
print("Try to guess my number.")

play_again = "y"

while play_again.lower() == "y":
    
    magic_number = random.randint(1,100)

    guess_count = 0

    guess = 0

    while guess != magic_number:
        guess = int(input("What is your guess? "))

        guess_count += 1

        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")
    print(f"Good job, {name}! It took you {guess_count} guesses!")

    play_again = input("Would you like to play again? (y/n) ")

print("Thank you for playing. Goodbye!")