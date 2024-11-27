"""from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Main Menu")

menubar = Menu(window)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=window.destroy)

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_separator()
edit.add_command(label="Find", command=None)
edit.add_command(label="Replace", command=None)

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Help",menu=edit)
help.add_command(label="About Tk", command=None)
help.add_command(label="Why Tk", command=None)
help.add_command(label="Demo", command=None)
help.add_separator()
help.add_command(label="Troubleshooting", command=None)
help.add_command(label="Other Tk Projects", command=None)

window.config(menu=menubar)
mainloop()"""

from tkinter import *
from tkinter.ttk import *

window = Tk()

progress = Progressbar(window, orient = HORIZONTAL,length = 100, mode="determinate")

def bar():
    import time
    progress["value"] = 20
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 30
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 40
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 50
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 60
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 70
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 80
    window.update_idletasks()
    time.sleep(1)

    import time
    progress["value"] = 90
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 100

progress.pack(pady=10)

Button(window, text="Start", command=bar).pack(pady=10)

mainloop()