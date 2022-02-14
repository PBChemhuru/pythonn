import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.ttk import Combobox

from pytube import YouTube
from tkinter import messagebox as mb


# function to search for video
def findvid():
    link = entry.get()
    try:
        yt = YouTube(link)
    except:
        mb.showerror("Error", "Please enter link or Check your Connection ")

    mb.showinfo('Video Found', yt.title + " by " + yt.author)


def Browse():
    download_Directory = filedialog.askdirectory()
    download_strVar.set(download_Directory)


def downloadvid():
    download_folder = download_strVar.get()
    link = entry.get()
    try:
        yt = YouTube(link)
    except:
        mb.showerror("Error", "Please enter link or Check your Connection ")
    option = form.get()
    if option == "720p":
        ys = yt.streams.filter(progressive=True).order_by("resolution").desc().first()
        ys.download(download_folder)
        mb.showinfo("Downloader", "Download complete")
    elif option == "360p":
        ys = yt.streams.get_by_itag('18')
        ys.download(download_folder)
        mb.showinfo("Downloader", "Download complete")
    else:
        ys = yt.streams.filter(type="audio").order_by('abr').desc().first()
        ys.download(download_folder)
        mb.showinfo("Downloader", "Download complete")


# creation of gui window
window = tk.Tk()
window.geometry('350x150')
window.resizable(False, False)
window.title("Youtube downloader")
window.iconbitmap("YouTube_23392.ico")

# title = tk.Label(window, text="Youtube Downloader", bg="red", fg="white").grid(row=0, column=2)
# creation gui widgets
# links labels and entry
link_label = tk.Label(window, text="Link: ").grid(row=3, column=0)
link_strVar = tk.StringVar(window)
entry = tk.Entry(window, textvariable=link_strVar)
entry.grid(row=3, column=2)
# download label and entry
downloadPath_label = tk.Label(window, text="Download Path :").grid(row=4, column=0)
download_strVar = tk.StringVar(window)
download = tk.Entry(window, textvariable=download_strVar)
download.grid(row=4, column=2)

format_label = tk.Label(window, text="Format: ").grid(row=5, column=0)
# creation of buttons
browse_button = tk.Button(window, text="Browse", command=lambda: Browse()).grid(row=4, column=3)
download_button = tk.Button(window, text="Download", command=lambda: downloadvid(), bg="red", fg="white").grid(row=6,
                                                                                                               column=2)
search_button = tk.Button(window, text="Search", command=lambda: findvid(), bg="red", fg="white").grid(row=7, column=2)
# creation of combobox
n = tk.StringVar()
form: Combobox = ttk.Combobox(window, width=27, textvariable=n)
form['values'] = ("720p", "360p", "mp3")
form.grid(row=5, column=2)
form.current(0)

window.mainloop()
