# using with in python 

with open('abc.txt','r') as file:
    print(file.read())

# read only few characters
try:
    with open('abc.txt','r') as f:
        print(f.read(2))
except FileNotFoundError:
    print("File does not exist")

with open('abc.txt','r') as f:
    v=f.readlines()
    for i in v:
        word=i.split()
        print(word)

