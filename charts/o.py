import random

options = ("stone", "paper", "scissors")

round = 1
computer_wins = 0
user_wins = 0

while True:
    print("*" * 10)
    print("ROUND", round)
    print("*" * 10)

    user_option = input("Stone, paper or scissors => ").lower()

    round += 1

    if not user_option in options:
      print("This option it does not work")
      continue

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)

    if user_option == computer_option:
      print("Tie")
    elif user_option == "stone":
        if computer_option == "scissors":
            print("The stone win to scissors")
            print("User win")
            user_wins += 1
        else:
            print("The paper win to stone")
            print("Computer win")
            computer_wins += 1
    elif user_option == "paper":
        if computer_option == "stone":
            print("The paper win to stone")
            print("User win")
            user_wins += 1
        else:
            print("The scissors win to paper")
            print("Computer win")
            computer_wins += 1
    elif user_option == "scissors":
        if computer_option == "paper":
            print("The scissors win to paper")
            print("User win")
            user_wins += 1
        else:
            print("The stone win to scissors")
            print("Computer win")
            computer_wins += 1


        if user_wins == 2:
            print("User wins")
            break

        if computer_wins == 2:
            print("Computer wins")
            break

    

