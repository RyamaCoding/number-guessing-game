# Create a number guessing game
# engine chooses a random number between 1 and 100 but does not display it
# easy or hard mode. easy = 10 attempts. hard = 5 attempts.
# as each attempt is wrong the number of attempts goes down
# tell user if too high or too low and to guess again

import random

print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100")
guessed_number = random.randint(1,100)
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

def user_attempts():
    if difficulty_choice == 'easy':
        attempts = 10
    elif difficulty_choice == 'hard':
        attempts = 5
    else: 
        print("Invalid choice. Choose one of the two options.")
        return
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
    
        if user_guess > guessed_number:
            print("Too high.")
        elif user_guess < guessed_number:
            print("Too low.")
        else:
            print(f"Congratulations! You guessed the number correctly. The correct number was {guessed_number}.")
            return

        attempts -= 1

        if attempts == 0:
            print(f"You have run out of guesses. The correct number was {guessed_number}.")
            return
        elif attempts > 0:
            print("Guess again.")
    
user_attempts()