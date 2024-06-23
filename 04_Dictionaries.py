# dictionary have a key value pair 
def get_choices():
    player_choice=input("enter your choice(rock, paper,scissors)")
    computer_choices="rock"
    choice={"player":player_choice,"computer":computer_choices}
    return choice

print(get_choices())
'''
fav_color="blue"
age=20
dict={
    "name":"hello",
    "color":fav_color,
    "age":age
      }
print(dict.get("age"))
'''



