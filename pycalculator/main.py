import parser
from math import factorial
from tkinter import *

i = 0


def get_variable(num):
    global i
    expression_field.insert(i, num)
    i += 1


def get_op(op):
    global i
    expression_field.insert(i, op)
    i += 1


def clear_all():
    expression_field.delete(0, END)


def undo():
    entire_string = expression_field.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        expression_field.insert(0, new_string)
    else:
        clear_all()
        expression_field.insert(0, "Error")


def fact():
    entire_string = expression_field.get()
    try:
        res = factorial(int(entire_string))
        clear_all()
        expression_field.insert(0, res)
    except Exception:
        clear_all()
        expression_field.insert(0, "Error")


def eva():
    entire_string = expression_field.get()
    try:
        a = parser.expr(entire_string).compile()
        res = eval(a)
        clear_all()
        expression_field.insert(0, res)
    except Exception:
        clear_all()
        expression_field.insert(0, "Error")


window = Tk()
window.configure(background="white")
window.title("Calculator")
window.geometry("250x180")
equation = StringVar()
expression_field = Entry(window, textvariable=equation, bg="light green")
expression_field.grid(columnspan=4, ipadx=60)
number_one = Button(window, text="1", fg="blue", bg="black", command=lambda: get_variable(1), height=1, width=7)
number_one.grid(row=1, column=0)
number_two = Button(window, text="2", fg="blue", bg="black", command=lambda: get_variable(2), height=1, width=7)
number_two.grid(row=1, column=1)
number_three = Button(window, text="3", fg="blue", bg="black", command=lambda: get_variable(3), height=1, width=7)
number_three.grid(row=1, column=2)
number_four = Button(window, text="4", fg="blue", bg="black", command=lambda: get_variable(4), height=1, width=7)
number_four.grid(row=2, column=0)
number_five = Button(window, text="5", fg="blue", bg="black", command=lambda: get_variable(5), height=1, width=7)
number_five.grid(row=2, column=1)
number_six = Button(window, text="6", fg="blue", bg="black", command=lambda: get_variable(6), height=1, width=7)
number_six.grid(row=2, column=2)
number_seven = Button(window, text="7", fg="blue", bg="black", command=lambda: get_variable(7), height=1, width=7)
number_seven.grid(row=3, column=0)
number_eight = Button(window, text="8", fg="blue", bg="black", command=lambda: get_variable(8), height=1, width=7)
number_eight.grid(row=3, column=1)
number_nine = Button(window, text="9", fg="blue", bg="black", command=lambda: get_variable(9), height=1, width=7)
number_nine.grid(row=3, column=2)
plus = Button(window, text="+", fg="blue", bg="black", command=lambda: get_op("+"), height=1, width=7)
plus.grid(row=4, column=2)
minus = Button(window, text="-", fg="blue", bg="black", command=lambda: get_op("-"), height=1, width=7)
minus.grid(row=2, column=3)
divide = Button(window, text="/", fg="blue", bg="black", command=lambda: get_op("/"), height=1, width=7)
divide.grid(row=3, column=3)
multiply = Button(window, text="*", fg="blue", bg="black", command=lambda: get_op("*"), height=1, width=7)
multiply.grid(row=4, column=3)
decimal = Button(window, text=".", fg="blue", bg="black", command=lambda: get_variable("."), height=1, width=7)
decimal.grid(row=4, column=0)
number_zero = Button(window, text="0", fg="blue", bg="black", command=lambda: get_variable(0), height=1, width=7)
number_zero.grid(row=4, column=1)
backspace = Button(window, text="Del", fg="blue", bg="black", command=lambda: undo(), height=1, width=7)
backspace.grid(row=1, column=3)
percent = Button(window, text="%", fg="blue", bg="black", command=lambda: get_op("%"), height=1, width=7)
percent.grid(row=5, column=1)
squared = Button(window, text="^2", fg="blue", bg="black", command=lambda: get_op("**2"), height=1, width=7)
squared.grid(row=5, column=2)
fact = Button(window, text="x!", fg="blue", bg="black", command=lambda: fact(), height=1, width=7)
fact.grid(row=5, column=0)
AC = Button(window, text="AC", fg="blue", bg="black", command=lambda: clear_all(), height=1, width=7)
AC.grid(row=5, column=3)
equal = Button(window, text="=", fg="blue", bg="black", command=lambda: eva(), height=1, width=7)
equal.grid(row=6, column=0, columnspan=4, ipadx=92)

window.mainloop()
