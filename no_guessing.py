import random

def number_guessing_game():
    small = int(input("Enter smaller number of the range: "))
    big = int(input("Enter bigger number of the range: "))

    if small >= big:
        print("wrong range try again")
        return

    secret_number = random.randint(small, big)
    attempts = 0

    print(f"\nGuess a number between {small} and {big}.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thanks for playing!")

number_guessing_game()