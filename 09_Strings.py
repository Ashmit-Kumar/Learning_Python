F_name="Roronoa"
L_name="Zoro"
print(F_name+" "+L_name) # Concatenation using + operator 


#appending the String
name="Monkey"
name+=" D."
name+=" Luffy"
print(name)

# casting
age=str(49)
print(age)

#multi line String
print("""
     This is multi Line String 
      hello
"""
)
print(''''
     This is multi Line String 
      hello
'''
)


# every fuction return a new modified string it doesn't change anything in original string
print("ADD".islower())
s="AAAAAAa"
ss="Ashmit"
s1="AA"
s2="  aaaa bbbbabb cccc"
print(s.upper()) 
print(s.lower())
print(s1.islower())
print("Aa" in s)
print(s1.isupper())
print(s2.title())
print(s2.startswith("aaa"))
print(s.startswith("A"))
print(s.endswith("Aa"))
print(ss.replace("shm","mhs")) #here you pass the substring you want to change with the new substring 
# print(ss.replace(0,'k')) error 
print(ss.replace("As",''))  

print(s2.split('a'))
print(s2.split(' ',1))
print(s2.split(' ',2))
print(s2.split(' ',0))
print(s2.split(' '))

print(s2.strip())  #It's like a trim function in java
ss1="-"
print(ss1.join('Hello')) #h-e-l-l-o
list1=["a","s","h","m","i","t"]
print("".join(list1))
# https://www.youtube.com/watch?v=eWRfhZUzrAc&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB
# 1:16:40

words=["apple","banana","cherry",""]
separator="@ "
result=separator.join(word for word in words)
print(result)
'''
dic = {1:'Geek', 2:'For', 3:'Geeks'}

# Joining special character with dictionary
string = '_'.join(dic)

print(string)

Hangup (SIGHUP)
Traceback (most recent call last):
  File "Solution.py", line 4, in <module>
    string = '_'.join(dic)
TypeError: sequence item 0: expected string, int found


'''



# Escaping Characters


# name="Be"au"
# it will show error 

name="Be\"au" #use a backslash to correct 
print(name)
name1="Be\nea"
name2="Be\\ea"

a="long long road"
print(name[0],name[1],name[-1])
print(a[1:3])
print(a[:7])
print(a[3:])

# to get the ascii value of a character 
#n="c",
#print(ord(n))
n='c',
print(ord('c')) # this will give ascii value but you will pass the character directly 