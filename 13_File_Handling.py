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
'''

