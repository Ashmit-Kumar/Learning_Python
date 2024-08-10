a=['a','b','c','d','e']

for i in range(0,len(a),2):
    print(a[i])

for i in range(len(a)):
    print(a[i])

count=0
while count<=9:
    print(f'counter is {count}')
    count+=1


c=1
while c>0 and c<2:
    print(c)
    c+=1
else:
    print("bhk")


d={"1":1,"2":2,"3":3}

for value in d:
    print(value)


for i in range(1,5):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(1,5):
    print('*'*i)
for i in range(4,0,-1):
    print("*"*i)