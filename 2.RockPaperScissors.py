import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}.")
  if player == computer:
    return ("It's a Tie")
    
  elif player == "rock": 
    if computer == "scissors":
      return("Rock smashs scissors! You Win!")
      
    else: 
      return("Paper covers Rock! You Lose!")
      
  elif player == "paper":
    if computer == "rock":
      return("Paper Covers Rock! You Win!")
      
    else: 
      return("Scissors Cuts Paper! You Lose!")
      
  elif player == "scissors": 
    if computer == "paper":
      return("Scissors Cuts Paper! You Win!")
      
    else: 
      return("Rock smashes scissors! You Lose!")


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
