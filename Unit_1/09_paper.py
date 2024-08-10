import tkinter as tk
from functools import partial

def click_digit(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + digit)

def click_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

def click_clear():
    entry.delete(0, tk.END)

def click_equals():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button definitions and their grid positions
buttons = [
    ('7', 1, 0, 'digit'), ('8', 1, 1, 'digit'), ('9', 1, 2, 'digit'), ('/', 1, 3, 'operator'),
    ('4', 2, 0, 'digit'), ('5', 2, 1, 'digit'), ('6', 2, 2, 'digit'), ('*', 2, 3, 'operator'),
    ('1', 3, 0, 'digit'), ('2', 3, 1, 'digit'), ('3', 3, 2, 'digit'), ('-', 3, 3, 'operator'),
    ('0', 4, 0, 'digit'), ('.', 4, 1, 'digit'), ('+', 4, 2, 'operator'), ('=', 4, 3, 'equals'),
    ('C', 5, 0, 'clear')  # Clear button spans all columns
]

# Create and place buttons in the grid
for (text, row, column, button_type) in buttons:
    if button_type == 'clear':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=click_clear)
        button.grid(row=row, column=column, columnspan=4)  # Span all columns for 'C'
    elif button_type == 'equals':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=click_equals)
        button.grid(row=row, column=column)
    elif button_type == 'digit':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                          command=partial(click_digit, text))
        button.grid(row=row, column=column)
    elif button_type == 'operator':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                          command=partial(click_operator, text))
        button.grid(row=row, column=column)

# Run the Tkinter event loop
root.mainloop()
