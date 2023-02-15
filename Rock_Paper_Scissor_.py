import random

print("Welcome to Rock-Paper-Scissors!")

options = ["rock", "paper", "scissors"]
PLAYER_CHOICE = 0
COMPUTER_SCORE = 0

while True:
    # Get player input
    PLAYER_CHOICE = input("Enter your choice (rock/paper/scissors): ").lower()

    # Validate player input
    if PLAYER_CHOICE not in options:
        print("Invalid choice, please try again.")
        continue

    # Generate computer choice
    computer_choice = random.choice(options)

    # Display choices
    print(f"You chose {PLAYER_CHOICE}, and the computer chose {computer_choice}.")

    # Determine winner
    if PLAYER_CHOICE == computer_choice:
        print("It's a tie!")
    elif (PLAYER_CHOICE == "rock" and computer_choice == "scissors") or (PLAYER_CHOICE == "paper" and computer_choice == "rock") or (PLAYER_CHOICE == "scissors" and computer_choice == "paper"):
        print("You win!")
        PLAYER_CHOICE += 1
    else:
        print("You lose!")
        COMPUTER_SCORE += 1

    # Display score
    print(f"Score: Player {PLAYER_CHOICE}, Computer {COMPUTER_SCORE}")

    # Ask to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "n":
        break

print("Thanks for playing!")
