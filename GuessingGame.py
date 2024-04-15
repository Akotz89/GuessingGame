#Aaron Kotz, CIS261, GuessingGame

import random

def display_heading():
    print("Welcome to the Guessing Game!")
    print("-------------------------------")

def play_game():
    while True:
        try:
            limit = int(input("Enter the upper limit for the random number: "))
            if limit <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    number_to_guess = random.randint(1, limit)
    print(f"Guess the number between 1 and {limit}")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < number_to_guess:
                print("Your guess is too low. Try again.")
            elif guess > number_to_guess:
                print("Your guess is too high. Try again.")
            else:
                print("Congratulations! You've guessed the correct number.")
                break
        except ValueError:
            print("Please enter a valid integer.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")

def main():
    display_heading()
    play_game()

if __name__ == "__main__":
    main()

