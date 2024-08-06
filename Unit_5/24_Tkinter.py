from tkinter import *

# Positioning with Tkinter Grid System
root=Tk()

label=Label(root,text="This is a label")

label2=Label(root,text="This is second label")

# label.pack()
label.grid(row=0,column=0)
label2.grid(row=1, column=1)# row and colunms are realative to each other so if there is nothing in that row or column tkinter will ignore it  for ex label.grid(row=10,column=10) will be same as label.grid(row=0,column=0) as there is nothing in row 0,1...10 and column 0,1....


'''
label=Label(root,text="This is second label")
label.grid(row=0,column=0)
This  can be written as

label=Label(root,text="Hello").grid(row=1,column=1)
'''


root.mainloop()