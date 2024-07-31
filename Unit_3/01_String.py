l=[1,2,4,5]
l.insert(1,3)
print(l)
# l1=["a","b"]
# l.extend(l1)
print(l)
l.remove(4)
print(l)
l.sort(reverse=True)
print(l)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
mytuple.count('apple')

d={0:"zero",1:"one",2:"two",3:"three"}
keySeq={'a','b'}
valueSeq=1
d2=dict.fromkeys(keySeq)
d1=dict.fromkeys(keySeq,valueSeq)
print(d1)
print(d.items())
print(d.pop(0))
print(d.popitem())
print(d)