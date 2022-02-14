import time
from tkinter import *
from tkinter import messagebox as mb
from plyer import notification

window = Tk()
window.geometry("400x80")
window.title("Countdown Timer")

# create labels
hr_label = Label(window, text="Hours").grid(row=2, column=0)
min_label = Label(window, text="Minutes").grid(row=2, column=1)
sec_label = Label(window, text="Seconds").grid(row=2, column=2)
# create entry boxes
hours = StringVar()
minutes = StringVar()
seconds = StringVar()
hours.set(00)
minutes.set(00)
seconds.set(00)
hour_entry = Entry(window, textvariable=hours).grid(row=3, column=0)
min_entry = Entry(window, textvariable=minutes).grid(row=3, column=1)
sec_entry = Entry(window, textvariable=seconds).grid(row=3, column=2)


def startcount():
    try:
        Temp = (int(hours.get()) * 3600) + (int(minutes.get()) * 60) + int(seconds.get())

    except:
        mb.showerror("Invalid Error", "Please input the right value")
    while Temp > -1:
            mins, secs = divmod(Temp, 60)
            hrs = 0
            if mins > 60:
                hrs, mins = divmod(mins, 60)
            hours.set("{0:2d}".format(hrs))
            minutes.set("{0:2d}".format(mins))
            seconds.set("{0:2d}".format(secs))
            window.update()
            time.sleep(1)
            if Temp == 0:
                notification.notify(
                    title="Time Up",
                    message="Count down complete",
                    timeout=15
                )
            Temp -= 1


start = Button(window, text="Start Countdown", command=lambda: startcount()).grid(row=4, columnspan=3, ipadx=150)

window.mainloop()
