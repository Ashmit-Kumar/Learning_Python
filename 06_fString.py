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
'''
age1=45454
print("{age1}")
// If you will use the way i am using above it will print age1 not the value of the age1 just the age1
print(f"{age1}")


age=100005264112
print(f"{age}")
// if you will do this way by Adding f before it will print the value of age
'''