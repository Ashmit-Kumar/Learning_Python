from tkinter import *

# Function to update the display
def click(event):
    text = event.widget.cget("text")
    current = entry.get()
    if text == "=":
        try:
            result = eval(current)  # Evaluate the mathematical expression
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, text)

# Creating main window
root = Tk()
root.title("Simple Calculator")

# Entry widget to show the input and result
entry = Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place buttons in the grid
row_val = 1
col_val = 0
for button in buttons:
    btn = Button(root, text=button, font=('Arial', 18), width=4, height=2)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind('<Button-1>', click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter event loop
root.mainloop()
