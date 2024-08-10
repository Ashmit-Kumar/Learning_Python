''' 
# File should exist then only you will be able to read it
Read Operation:

1)read()
2)readline()
3)readlines()


'''
# read()
try:
    f=open('ab.txt','r')
    v=f.read()
    print(v)
except FileNotFoundError:
    print("file doesn't exist")
finally:
    f.close()


try:
    f=open('abc.txt','r')
    for line in f:
        print(line.strip())
except FileNotFoundError:
    print('File does not exist')
finally:
    f.close()


try:
    f=open('abc.txt','r')
    v=f.readline()
    print(v)
except FileNotFoundError:
    print("file does not exist")
finally:
    f.close()


try:
    f=open('z.txt','r')
except FileNotFoundError:
    print("File does not exist")
finally:
    f.close()

    