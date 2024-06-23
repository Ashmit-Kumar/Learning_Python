import random

def get_choices():
    player_Choice=input("Enter your choice(rock ,paper, scissor)")
    option=["Rock","Paper","Scissor"]
    computer_choice=random.choice(option).lower()
    choice={"Player":player_Choice,"Computer":computer_choice}
    # print(choice)
    win=check_win(player_Choice,computer_choice)
    return win

def check_win(player,computer):
    print("you chose "+player+" computer chose "+computer)
    print()
    if player==computer:
        return "It's a tie! "


result=get_choices()
print(result)