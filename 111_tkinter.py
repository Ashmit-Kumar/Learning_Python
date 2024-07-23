from tkinter import *

# Function to update the expression on the screen
def btn_click(char):
    global expression
    expression = expression + str(char)
    input_field.set(expression)

# Function to clear the display
def btn_clear():
    global expression
    expression = ""
    input_field.set("")

# Function to evaluate the expression
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_field.set(result)
        expression = result
    except:
        input_field.set("Error")
        expression = ""

# Main function
expression = ""
window = Tk()
window.title("Simple Calculator")

# Input field
input_field = StringVar()
input_box = Entry(window, textvariable=input_field, width=30, borderwidth=5)
input_box.grid(columnspan=4, ipadx=70)

# Buttons
button_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
row = 1
col = 0
for button_text in button_list:
    button = Button(window, text=button_text, command=lambda char=button_text: btn_click(char), width=5)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = Button(window, text="C", command=btn_clear, width=5)
clear_button.grid(row=5, column=0)

# Equal button
equal_button = Button(window, text="=", command=btn_equal, width=5)
equal_button.grid(row=5, column=3)

window.mainloop()
