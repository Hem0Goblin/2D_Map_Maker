# Imports
from tkinter import *
from tkinter import messagebox

val = 2


def raise_frame(frame_name):
    frame_name.tkraise()


# Functions For f1
def Load_it():
    global entry
    File_name = entry.get() + ".txt"
    try:
        with open(File_name, 'r'):
            print("File exists")
            print("Loading " + File_name)
        with open("storage.txt", 'w') as Load:
            Load.write(File_name)

    except FileNotFoundError:
        messagebox.showerror("FileNotFoundError", "File Not Found\nTry Another File Name")


def Cancel():
    with open("storage.txt", 'w') as Empty_file:
        Empty_file.write("")
    quit()


# Functions For f2
def enter_size():
    try:
        entry1, entry2 = int(e1.get()), int(e2.get())
        size = str(entry1) + " x " + str(entry2)
        Lb.insert(1, "Size of the map is: " + size)
        dims = (int(e1.get()), int(e2.get()))
        print(dims)
        with open("size.txt", 'w') as Map_size:
            Map_size.write(e1.get() + " " + e2.get())
        with open("storage.txt", 'w') as Empty_map:
            Empty_map.write("")
    except ValueError:
        messagebox.showerror("Type Error", "Inputs must be integers ")


def reset():
    Lb.delete(0, END)


# Main Loop
root = Tk()
resolution = (240, 105)
root.title("Arrange Map")

root.geometry(str(resolution[0]) + "x" + str(resolution[1]))
f1 = Frame(root)
f2 = Frame(root)

# Label and Entries for f1
top_space_1 = Frame(f1)
top_space_1.pack(side=TOP)

empty = Label(top_space_1, text="  ~~~~~~~~~~~~", relief=FLAT)
empty.pack(side=TOP)

upper_frame_1 = Frame(f1)
upper_frame_1.pack(side=TOP)

lower_frame_1 = Frame(f1)
lower_frame_1.pack(side=TOP)

x_label = Label(upper_frame_1, text="      Load File: ", relief=FLAT)
x_label.pack(side=LEFT)

entry = Entry(upper_frame_1, width=20)
entry.pack(side=LEFT)
entry.insert(0, "FileNameHere")

x_label = Label(upper_frame_1, text=".txt", relief=FLAT)
x_label.pack(side=RIGHT)

# Label and Entries for f2

upper_frame = Frame(f2)
upper_frame.pack(side=TOP)

lower_frame = Frame(f2)
lower_frame.pack(side=TOP)

Lb = Listbox(f2, relief=FLAT, width=25)
Lb.pack(side=BOTTOM)

e1 = Entry(upper_frame, width=12)
e1.pack(side=LEFT)
e1.insert(0, "Height")

x_label = Label(upper_frame, text=" x ", relief=FLAT)
x_label.pack(side=LEFT)

e2 = Entry(upper_frame, width=12)
e2.pack(side=RIGHT)
e2.insert(0, "Length")

# Buttons for f1
myButton = Button(lower_frame_1, text="Cancel", command=Cancel, relief=RAISED)
myButton.pack(side=RIGHT)
myButton = Button(lower_frame_1, text="Load it", command=Load_it, relief=RAISED)
myButton.pack(side=RIGHT)

# Buttons for f2
myButton = Button(lower_frame, text="Set Size", command=enter_size, relief=RAISED, cursor="sizing")
myButton.pack(side=LEFT)
myButton = Button(lower_frame, text="reset", command=reset, relief=RAISED)
myButton.pack(side=LEFT)

# Splitting To Pages
for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Create New Map', command=lambda: raise_frame(f2)).pack()
Button(f2, text='Load Map', command=lambda: raise_frame(f1)).pack()

if val == 1:
    raise_frame(f1)
if val == 2:
    raise_frame(f2)

root.mainloop()
