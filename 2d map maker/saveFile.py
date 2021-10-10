# Imports
from tkinter import *
from tkinter import messagebox
import random

# Main Loop
root = Tk()
resolution = (250, 85)
root.geometry(str(resolution[0]) + "x" + str(resolution[1]))
root.title("Save Map")

top_space = Frame(root)
top_space.pack(side=TOP)

empty = Label(top_space, text="~~~~~~~~~~~~", relief=FLAT)
empty.pack(side=TOP)

upper_frame = Frame(root)
upper_frame.pack(side=TOP)

lower_frame = Frame(root)
lower_frame.pack(side=TOP)

x_label = Label(upper_frame, text="Save This File As: ", relief=FLAT)
x_label.pack(side=LEFT)

entry = Entry(upper_frame, width=12)
entry.pack(side=LEFT)
name = random.randint(1000, 9999)
entry.insert(0, str(name))

x_label = Label(upper_frame, text=".txt", relief=FLAT)
x_label.pack(side=RIGHT)


def Save_it():
    global entry
    forbidden = """\/:*"<>|"""
    File_name = entry.get()+".txt"
    permission = 1
    for i in list(File_name):
        if str(i) in forbidden:
            messagebox.showerror("NonValid Name", """File name can not contain following:\n \ / : *  " < > |""")
            permission = 0

    if permission == 1:
        with open("storage.txt", 'w') as write:
            write.write(File_name)


def Throw_away():
    with open("storage.txt", 'w') as Empty_file:
        Empty_file.write("")
    quit()


myButton = Button(lower_frame, text="Save Map", command=Save_it, relief=RAISED)
myButton.pack(side=LEFT)
myButton = Button(lower_frame, text="Throw Away", command=Throw_away, relief=RAISED, cursor="sizing")
myButton.pack(side=LEFT)


# root.mainloop()
