fruits=['apple','banana','orange']
print(fruits[0])
print(fruits[-1])

print(fruits[0:2])

a=[1,2,3,4,5,6,7,8,9,10]
print(a[-4:-1])

a[3]=89
print(a)
a.extend([98,90,999])
print(a)
a.append(4)
print(a)
print(len(a))
contains=8 in a
b=[0,0,0,9]
a=a+b
print(contains)
print(a)
a.insert(2,22222)
print(a)
a.sort(reverse=True)
print(a)
c=a.copy()
print(c.count(0))

