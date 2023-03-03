import random

def choose_options():
  options = ("stone", "paper", "scissors")
  user_option = input("stone, paper or scissors => ").lower()
 
  if not user_option in options:
    print("This option not is valid")
    # continue
    return None, None
    
  computer_option = random.choice(options)
  
  print("user option =>", user_option)
  print("computer option =>", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Tie")
  elif user_option == "stone":
    if computer_option == "scissors":
      print("Stone win to scissors")
      print("user win")
      user_wins += 1
    else:
      print("Paper win to stone")
      print("Computer win")
      computer_wins += 1
  elif user_option == "paper":
    if computer_option == "stone":
      print("Paper win to stone")
      print("user win")
      user_wins += 1
    else:
      print("scissors win to paper")
      print("Computer win")
      computer_wins += 1
  elif user_option == "scissors":
    if computer_option == "paper":
      print("Scissors win to paper")
      print("user win")
      user_wins += 1
    else:
      print("Stone win to scissors")
      print("Computer win")
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print("The winner is computer")
      break

    if user_wins == 2:
      print("The winner is user")
      break

run_game()
        