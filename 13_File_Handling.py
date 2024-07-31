'''
File: It is a collection of bytes stored in some storage device like Harddisk, floppydisk,pendrive etc.

There are two types of file
1) Text File 
2) Binary File

1) Text File: In the text file the data is stored in ascii code or unicode format.
Whenever read or write operation takes place the data is first translated into machine readable format
Each Line of the file ends with a special character called end of the line

2) Binary File: In the binary file the data is stored in the binary format 

There is no need of translating the data as data is already in the binary format
 
There is no special character at the end of line


File access mode(Text File)
r(read only):opens an existing file if that file doesn't exist gives i/o error.
w(write only):creates a new file in writing mode and if that file exist deletes all it's previous content and adds new content to the file. 
a(append):creates a new file in writing mode if a file already exists then it retains the previous data and adds new data after the previous data.


File access mode(Binary File):
rb(read only):opens an existing file in reading mode if that file doesn't exist then gives i/o error.
wb(write only):creats a new file in writing mode if that file already exists then delete all the previous data and then add new content in it.
ab(append):creates a new file in writing mode and if that file exists than simply adds the data to the existing data

Text/Binary
rt/rbt(read and write)
wt/rbt(read and write)
at/rbt(append and read)


#Open a File
#open("filename",filemode)  
#by default it open a file in reading mode

Reading content of a file
There are three types of read function to read content in a python file

1 read()
2 readline()
3 readlines()

1) read([n]):to read n bytes from a file if n is missing, read the entire file content
'''
f=open('a.txt','w')
f.write("Helllo how aare you")
f.close()
f=open("abc.txt","r")
v=f.read() # read whole file
print(v)
f.close()

f=open("abc.txt","r")
v=f.read(10) #reads first 10 character of a file
print(v)
f.close()


f=open("abc.txt","r")
v=f.readline() #read first line
print(v)
f.close()

f=open("abc.txt","r")
for i in f:
    print(i+":")
f.close()

f=open("abc.txt","r")
v=f.readlines()
print(v)
f.close()


f=open("abc.txt","r")
v=f.read()
c=0
for i in v:
    if i==' ':
        c+=1
f.close()
print(c)


f=open('abc.txt','r')
v=f.read()
vowels=0
alpha=0
alpha2=0
for i in v:
    # print(i)
    # if i in 'a' or i in 'e' or i=='i' or i=='o' or i=='u':
    #     vowels+=1
    #if i in ['a','e','i','o','u']
    if i in 'aeiouAEIOU':
        vowels+=1
    if i.isalpha():
        alpha+=1
print(vowels)
print(alpha)
print(alpha2)
f.close()


f=open('abc.txt','r+t')
v=f.read()
while True:
    if v.find("aa"):
        print("mil gaya")
        break
    else:
        break
f.close()

f=open('abcd.txt','w')
f.write("Hello \n")
f.write("JJJJJ")
f.write("La La La \n")
f.close()
f=open('abcd.txt','r')
v=f.read()
f.close()
print(v)


f=open('abcd.txt','w')
l=['aaaaaaa','bbbbbbbbbbbbb','cccccc\n','ffffffff']
f.writelines(l)
f.close()

f=open('abcd.txt','r')
v=f.read()
f1=open('abcd.txt','w')
for i in v:
    f1.write(i+",")
read=f.read()
write=f.write(read)
f1.close()
f.close()

