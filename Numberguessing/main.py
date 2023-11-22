import random
import math
import tkinter as tk




def gen_numb():
    # selecting range
    global minimum
    global maximum
    global x
    global count
    count = 0
    print(count)
    minimum = lowrng.get()
    maximum = highrng.get()
    x = random.randint(minimum, maximum)
    print('Number = %d' % x)


def compare():
    global count
    count += 1
    n = guess.get()
    print('your guess = %d' % n)
    if x == n:
        my_result.set('Congratulations you win')
    elif x > n:
        my_result.set('your guess is too low')
    elif x < n:
        my_result.set('your guess is too high')
    if count >= 7:
        my_result.set("Game Over.The number is %d " % x)
        print("Game Over.The number is %d " % x)




# creation of gui window
window = tk.Tk()
window.geometry('500x300')
window.resizable(False, False)
window.title("Number Guessing Game")
window.iconbitmap('keyboard+123+regular-1330515566236956064.ico')
tk.Label(window, text='Enter the lower range: ').grid(row=1, column=0)
lowrng = tk.IntVar()
tk.Entry(window, textvariable=lowrng).grid(row=2, column=0)
tk.Label(window, text='Enter the upper range: ').grid(row=3, column=0)
highrng = tk.IntVar()
tk.Entry(window, textvariable=highrng).grid(row=4, column=0)
tk.Button(window, text='Generate', command=lambda: gen_numb(), bg='green', fg='white').grid(row=5, column=0)
tk.Label(window, text='Enter you guess').grid(row=6, column=0)
guess = tk.IntVar()
tk.Entry(window, textvariable=guess).grid(row=7, column=0)
tk.Button(window, text='Compare', command=lambda: compare(), bg='green', fg='white').grid(row=8, column=0)
tk.Button(window, text='Reset', command=lambda: gen_numb(), bg='green', fg='white').grid(row=9, column=0)
my_result = tk.StringVar()
tk.Label(window, textvariable=my_result, font="Courier 13 bold").grid(row=10, column=0)

window.mainloop()
