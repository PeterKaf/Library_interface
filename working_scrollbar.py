from tkinter import *

# Creating the root window
root = Tk()

# Creating a Canvas and attaching it to root window
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)

# Creating a Listbox and attaching it to the canvas
listbox = Listbox(canvas)
# Insert elements into the listbox
for values in range(100):
    listbox.insert(END, values)

# Creating a Scrollbar and attaching it to the canvas
scrollbar = Scrollbar(canvas, orient=VERTICAL)
# Attaching Listbox to Scrollbar
# Since we need to have a vertical scroll we use yscrollcommand
listbox.config(yscrollcommand=scrollbar.set)
# setting scrollbar command parameter
# to listbox.yview method its yview because
# we need to have a vertical view
scrollbar.config(command=listbox.yview)

# Using create_window method to add Listbox and Scrollbar on canvas
listbox_window = canvas.create_window((0, 0), window=listbox, anchor=NW)

# Wait until the listbox has been displayed and has a width
listbox.update()
listbox_width = listbox.winfo_width()

scrollbar_window = canvas.create_window((listbox_width, 0), window=scrollbar, anchor=NW)

# Setting the Scrollbar height to match the Listbox height
canvas.itemconfig(scrollbar_window, height=listbox.winfo_height())

# Binding a function to the Canvas resize event to update the Scrollbar height
def update_scrollbar_height(event):
    canvas.itemconfig(scrollbar_window, height=listbox.winfo_height())
canvas.bind('<Configure>', update_scrollbar_height)

root.mainloop()
