import random

def get_choices():
    player_Choice=input("Enter your choice(rock ,paper, scissor)")
    option=["Rock","Paper","Scissor"]
    computer_choice=random.choice(option)
    choice={"Player":player_Choice,"Computer":computer_choice}
    return choice


result=get_choices()
print(result)