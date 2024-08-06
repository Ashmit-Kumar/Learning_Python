from tkinter import *

# To input
root=Tk()
def myClick():
    label=Label(root,text=e.get())
    label.grid(row=2,column=2)
myButton=Button(root,text="Enter your name",command=myClick)
# e=Entry(root)
# e=Entry(root,width=50)
e=Entry(root,width=50,fg="blue",borderwidth=20)
myButton.grid(row=1,column=0)
e.grid(row=0,column=0)


root.mainloop()