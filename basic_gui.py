from tkinter import *  # importing tkinter module

root = Tk()  # creating root window

# root window title and dimensions
root.title("Welcome to Tkinter tutorial")

# set geometry (width x height)
root.geometry("350x200")

# adding menu bar in root window
# new item in menu bar labelled as New
# adding more items in menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
item.add_cascade(label="File", menu=item)
root.config(menu=menu)

# adding label to the root window
lbl = Label(root, text="Are you a Geek?")
lbl.grid()

# adding entry field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)


# function to display text when
# button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text=res)


# button widget with red color textlbl
btn = Button(root, text="Click Me", fg="red", command=clicked)

# set button grid
btn.grid(column=2, row=0)

# all widgets will be here
# Execute Tkinter
root.mainloop()
