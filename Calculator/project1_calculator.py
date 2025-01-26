#Tkinter is a standard GUI (Graphical User Interface) library for Python. It provides a set of tools and widgets for creating desktop applications with graphical interface.
from tkinter import *

# win = window
win = Tk()
win.title('Calculator')
win.geometry('350x350')
win.resizable(0, 0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear input field
def bt_clear():
    global expression
    expression = ''
    input_text.set('')

# Function to remove the last character (X button)
def bt_backspace():
    global expression
    expression = expression[:-1]  # Remove last character
    input_text.set(expression)

# Function for equal button
def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ''
    except:
        input_text.set('Error')
        expression = ''

# Grid used for spacing, aligning, row and column layouts.
expression = ''
input_text = StringVar()

input_frame = Frame(win, width=300, height=40)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 13, 'bold'), width=35, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Increase the height of the input field

btns_frame = Frame(win, width=300, height=200)
btns_frame.pack()

# First row (C, X, /)
clear = Button(btns_frame, text='C', width=23, height=3, command=lambda: bt_clear()).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
backspace = Button(btns_frame, text='X', width=10, height=3, command=lambda: bt_backspace()).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btns_frame, text='/', width=9, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Second row (7, 8, 9, *)
seven = Button(btns_frame, text='7', width=9, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text='8', width=9, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text='9', width=9, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text='*', width=9, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

# Third row (4, 5, 6, -)
four = Button(btns_frame, text='4', width=9, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text='5', width=9, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text='6', width=9, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text='-', width=9, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# Fourth row (1, 2, 3, +)
one = Button(btns_frame, text='1', width=9, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text='2', width=9, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text='3', width=9, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text='+', width=9, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# Fifth row (0, ., =)
zero = Button(btns_frame, text='0', width=20, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
dot = Button(btns_frame, text='.', width=9, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btns_frame, text='=', width=9, height=3, command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
#paddingx:horinzontal extraspace ,paddingy vertical extraspace
#5 rows,4columns
#in Tkinter, the .set() method is used to set the value of certain Tkinter variables, particularly variables associated with widgets like StringVar, IntVar, DoubleVar, etc. 

