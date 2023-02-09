import random


def get_choices():
  player_choice = input("Enter a choice (Rock, Paper, Scissors): ")
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer":   computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player} & computer chose {computer}")
  if player == computer:
    return "Its a tie"
  elif player == "Rock": #nested if/else
    if computer == "Scissors":
     return "Rock smahes Scissors! You Win"
    else:
     return "Paper covers Rock! You Lose"
  elif player == "Paper": #nested if/else
    if computer == "Scissors":
     return "Scissors cuts Paper! You Lose"
    else:
     return "Paper Covers Rock! You Win"    
  elif player == "Scissors": #nested if/else
    if computer == "Rock":
     return "Rock Breaks Scissors! You Lose"
    else:
     return "Scissors cut Paper! You Win"        

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



