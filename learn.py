import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors: )")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def check_win(player, computer):
    # print("You chose" + player + ", computer chose" + computer) # we can use an fstring
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose"
    elif player == "scissors":
        if computer == "paper":
            return  "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose"
    # elif player == "rock" and computer == "scissors":
    #     return "Rock smashes scissors! You win!"
    # elif player == "rock" and computer == "paper":
    #     return "Paper covers rock! You lose" #we can rewrite this to make it shorter

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)