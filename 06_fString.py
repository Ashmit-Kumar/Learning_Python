import random
def get_Choice():
    player_choice=input("Enter your Choice(Rock Paper Scissor)")
    options=['Rock','Paper','Scissor']
    computer_choice=random.choice(options)
    choice={
        "Player":player_choice,
        "Computer":computer_choice
    }   
    win=get_win(player_choice,computer_choice) 
    return win

def get_win(player,computer):
    print("Player Choice "+player+" Computer Choice "+computer)
    if player==computer:
        return "It's a Tie!😮😮😮"
    
result=get_Choice()
print(result)