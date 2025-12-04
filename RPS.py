import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if player_choice not in options:
        print("Invalid choice! Try again.")
        return get_choices()
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It is a tie!"  
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You lose!"

while True:  
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break

