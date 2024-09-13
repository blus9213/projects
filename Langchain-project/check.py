import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
         return f"You win with {player_choice} against {computer_choice}!"
    else:
         return f"You lose to {computer_choice}!"

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Main game loop
while True:
    player = get_user_choice()
    computer = get_computer_choice()

    print("Computer chose:", computer)
    result = determine_winner(player, computer)
    print(result)

    if input("Do you want to play another round? (Y/N): ").lower() != 'y':
        break
    else:  # Resetting for the next iteration of a new game.
        player = None  # Clears previous choice in case user re-enters their option without restarting script manually.