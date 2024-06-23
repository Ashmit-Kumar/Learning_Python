import random
def get_Choice():
    player_choice=input("Enter your Choice(Rock Paper Scissor)").lower()
    options=['Rock','Paper','Scissor']
    computer_choice=random.choice(options).lower()
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
    elif player=="rock" and computer=="scissor":
        return "Rock smashes Scissors you win"
    elif player=="rock" and computer=="paper":
        return "Paper folds Rock you loose"
    elif player=="paper" and computer=="rock":
        return "paper folds rock you win"
    elif player=="paper" and computer=="scissor":
        return "Scissors cut Paper you loose"
result=get_Choice()
print(result)

'''
if age==18:
    print("yay you are adult now")
elif age<18
    print("you are an teenager")
elif age>18:
    print("you are a big boy/girl")
else:
    print("you are not born")

// In python we  use and instead of && 
// IN python we use or instead of ||
// Not is same as java in pyhton !


a=0
b=3
if a!=b:
    print(True)

'''