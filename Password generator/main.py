from tkinter import *
import random


def passwordgenerate():
    wordstring = (word1.get() + word2.get() + word3.get()).strip()
    wordarr = list(wordstring)
    Passwordarr = []
    passlength=int(passlen.get())
    for x in range(passlength):
        k = random.randint(0, len(wordarr) - 1)
        Passwordarr.append(wordarr[k])
    Password = " ".join(Passwordarr)
    print(Password)
    labelpass = Label(window, text="Password:").grid(row=6, column=0)
    text_box = Text(window, height=1, width=20)
    text_box.grid(row=6, column=1)
    text_box.insert('end', Password)
    text_box.config(state='disabled')


window = Tk()
window.geometry("300x250")
window.title("Password Generator")

passlen = StringVar()
word1 = StringVar()
word2 = StringVar()
word3 = StringVar()

labeltitle = Label(window, text="Password Generator").grid(row=0, column=1)
lblpasslen = Label(window, text="Password Length:").grid(row=1, column=0)
entrypasslen = Entry(window, textvariable=passlen).grid(row=1, column=1)
labelword1 = Label(window, text="First Word:").grid(row=2, column=0)
entry1 = Entry(window, textvariable=word1).grid(row=2, column=1)
labelword2 = Label(window, text="Second Word:").grid(row=3, column=0)
entry2 = Entry(window, textvariable=word2).grid(row=3, column=1)
labelword3 = Label(window, text="Third Word:").grid(row=4, column=0)
entry3 = Entry(window, textvariable=word3).grid(row=4, column=1)
generate = Button(window, text="Generate", command=lambda: passwordgenerate()).grid(row=5, column=1)

window.mainloop()
