import random
def get_Choice():
    player_choice=input("Enter your Choice(Rock Paper Scissor)").lower()
    options=['Rock','Paper','Scissor']
    computer_choice=random.choice(options).lower()
    choice={
        "Player":player_choice,
        "Computer":computer_choice
    }   
    print(f"Player Choice {player_choice}, computer choice {computer_choice}")
    win=get_win(player_choice,computer_choice) 
    return win

def get_win(player,computer):
    print("Player Choice "+player+" Computer Choice "+computer)
    if player==computer:
        return "It's a Tie!😮😮😮"
    elif player=="rock":
        if computer=="scissor":
            return "Rock smashes Scissors you win"
        else:
            return "Paper folds Rock you loose"
    elif player=="paper" :
        if computer=="rock":
            return "paper folds rock you win"
        else:
            return "Scissors cut Paper you loose"
    else:
        if computer=="rock":
            return "Rock smashes Sissors You loose"
        else :
            return "scissor cuts paper"
result=get_Choice()
print(result)
