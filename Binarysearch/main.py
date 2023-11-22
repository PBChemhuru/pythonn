from numpy import random
import tkinter as tk
from tkinter import messagebox as mb


def binary_search():
    x=(searchkey.get())
    arr=num
    print(arr)
    print(x)
    low = 0
    high = len(arr) - 1
    found= False

    while low <= high and not found:
        mid = int(((high + low) / 2))
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            found=True
    if found ==True:
        mb.showinfo('Search complete', 'Element is present')
    else:
        mb.showinfo('Search complete', 'Element is not present in array')




num = random.randint(100, size=7)
num.sort()
# creation gui widgets
window = tk.Tk()
window.geometry('350x150')
window.resizable(True,True)
window.title("Binary Search")
tk.Label(window, text="Random Array").grid(row=1,column=8)
for i in range(0, len(num)):
    list_strVar = num[i]
    tk.Label(window,text=list_strVar).grid(row=2, column=i)
tk.Label(window, text='Enter value to search').grid(row=3,column=8)
searchkey=tk.IntVar()
tk.Entry(window, textvariable=searchkey).grid(row=4, column=8)
tk.Button(window, text='Search',command=lambda :binary_search(),bg='blue',fg='white').grid(row=5,column=8)



window.mainloop()


