# Dictionary

d={}
a={"One":1,"Two":2,"Three":3,"Four":4}

print(a["One"])
print(a.get("Four"))

a["One"]=11
print(a["One"])
print(a)
print(len(a))
remove=a.pop("One")
print(remove)
print(a)
remove2=a.popitem()
print(a)