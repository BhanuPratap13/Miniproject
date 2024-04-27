import random

entre = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {entre}, computer chose {computer_action}.\n")

if entre == computer_action:
    print(f"Both players selected {entre}. It's a tie!")
elif entre == "rock":
    if computer_action == "scissors":
        print(" You win!")
    else:
        print("Paper covers rock! You lose.")
elif entre == "paper":
    if computer_action == "rock":
        print("You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif entre == "scissors":
    if computer_action == "paper":
        print(" You win!")
    else:
        print("You lose.")