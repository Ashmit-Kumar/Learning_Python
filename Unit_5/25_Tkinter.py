from tkinter import *

# Creating Buttons
root = Tk()

def myClick():
    myLabel = Label(root, text="I got pressed")
    myLabel.grid(row=1,column=1)

myButton = Button(root, text="1")
myButton2 = Button(root, text="2", padx=20, pady=20)  # Adding padding to button
myButton3 = Button(root, text="3", command=myClick)

myButton.grid(row=0, column=0)
myButton2.grid(row=0, column=1)
myButton3.grid(row=0, column=2)

root.mainloop()
