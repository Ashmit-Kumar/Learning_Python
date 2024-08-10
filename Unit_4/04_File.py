# Manipulating File pointer

f=open('cse.txt','r')
f.seek(20)
print(f.tell())
print(f.readlines())
f.close()

f=open('cse.txt','rb')
f.seek(-10,2)
print(f.tell())
print(f.read().decode('utf-8'))
f.close()

f=open('cse.txt','r')
f.seek(10)
print(f.tell())
f.seek(-3,1)
print(f.tell())
# print(f.read())
f.close()