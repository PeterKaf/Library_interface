import json
import tkinter as tk
import Classes

db_name = "owned_books.json"
book_database = json.load(open(db_name, 'r'))
lib1 = Classes.Library('SampleLibrary1', book_database)

window = tk.Tk()
# bg_image = tk.PhotoImage(file="Background.png")
# bg_label = tk.Label(window, image=bg_image)
# bg_label.grid(row=0, column=0, sticky="nsew")

window.rowconfigure(0, weight=0)
window.columnconfigure(0, weight=0)
no_row = 18
no_cols = 35
# Create and configure rows
for i in range(no_row-1):
    window.grid_rowconfigure(i, minsize=50)

# Create and configure columns
for j in range(no_cols-1):
    window.grid_columnconfigure(j, minsize=50)

window.rowconfigure(no_row, weight=1, minsize=50)
window.columnconfigure(no_cols, weight=1, minsize=50)

for i in range(18):
    for j in range(35):
        frame = tk.Frame(window, highlightbackground="black", highlightthickness=1)
        frame.grid(row=i, column=j, sticky="nsew")

# ########################################################TRACKERS######################################################
is_but1_on = False
is_but2_on = False
is_but3_on = False
is_but4_on = False


# #########################################################CANVAS#######################################################
donatebox_canvas = tk.Canvas(window, width=310, height=200, borderwidth=5, relief="solid")
borrowbox_canvas = tk.Canvas(window, width=310, height=200, borderwidth=5, relief="solid")

# ########################################################FUNCTIONS#####################################################


def switch2_forget():
    global is_but2_on
    donatebox_canvas.grid_forget()
    donate_label.grid_forget()
    donate_accept_label.grid_forget()
    donate_accept_button.grid_forget()
    booklist_scroll.grid_forget()
    is_but2_on = False


def switch3_forget():
    global is_but3_on
    borrowbox_canvas.grid_forget()
    borrow_label.grid_forget()
    borrow_label_name.grid_forget()
    borrow_label_book.grid_forget()
    borrow_accept_button.grid_forget()
    is_but3_on = False


def button1_switch():
    global is_but1_on
    if is_but1_on:
        booklist.grid_forget()
        is_but1_on = False
    else:
        booklist.grid(column=29, row=4, rowspan=7, columnspan=12, padx=10, pady=5, sticky='nw')
        booklist_scroll.configure(command=booklist.yview)
        booklist_scroll.grid(column=35, row=4, rowspan=6, columnspan=3, sticky="ne", pady=5)
        booklist_scroll.set(0.0, 0.0)
        is_but1_on = True


def formatted_booklist(books):
    string = ""
    for book in books:
        if book == books[-1]:
            string += str(book)
        else:
            string += str(book) + "\n"
    return string


def button2_switch():
    global is_but2_on, donate_input

    if is_but2_on:
        switch2_forget()
    else:
        switch3_forget()
        donatebox_canvas.grid(column=2, row=3, rowspan=2, padx=(20, 0), pady=(20, 0))
        donatebox_canvas.create_window(110, 100, window=donate_input, width=200)
        donate_label.grid(column=2, row=3, rowspan=2, padx=(20, 0))
        donate_accept_button.grid(column=2, row=3, rowspan=2, padx=(20, 0), pady=(10, 20))
        is_but2_on = True


def read_donate():
    global donate_input, book_database
    x = donate_input.get()
    lib1.add_book(x)
    booklist.insert(tk.END, x)
    donate_accept_label.grid(column=2, row=4, columnspan=2, padx=(20, 0), pady=(20, 0))


def button3_switch():
    global is_but3_on, borrow_input_name, borrow_input_book

    if is_but3_on:
        switch3_forget()
    else:
        switch2_forget()

        borrowbox_canvas.grid(row=3, column=1, rowspan=2, padx=5, pady=5)
        borrow_input_name.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        borrow_input_book.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        borrow_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        borrow_label_name.grid(row=3, column=1, sticky="w")
        borrow_label_book.grid(row=3, column=1, sticky="w")

        borrow_accept_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        is_but3_on = True


def read_borrow():
    global borrow_input_name, borrow_input_book
    x = borrow_input_name.get()
    y = borrow_input_book.get()
    lib1.add_book(x)
    donate_accept_label.grid(row=2, column=1, sticky="w")


# def update_scrollbar_height(event):
#     tk.canvas.itemconfig(scrollbar_window, height=booklist.winfo_height())
# tk.canvas.bind('<Configure>', update_scrollbar_height)

# ######################################################CHOICE BUTTONS##################################################

choice_1 = tk.Button(window, text="Hide/Show Booklist", height=1, font=("Roman", "20"),
                     command=lambda: button1_switch())
choice_1.grid(row=10, column=30, columnspan=7, sticky="ne", padx=5, pady=5)

choice_2 = tk.Button(window, text="Donate a book", height=3, font=("Roman", "20"),
                     command=lambda: button2_switch())
choice_2.grid(row=5, column=0, rowspan=2, columnspan=6, sticky="nw", padx=5, pady=5)

donate_accept_button = tk.Button(window, text="Add book", font=("Roman", "11"),
                                 command=read_donate)

choice_3 = tk.Button(window, text="Borrow a book", height=3, font=("Roman", "20"),
                     command=lambda: button3_switch())
choice_3.grid(row=7, column=0, rowspan=2, columnspan=6, sticky="nw", padx=5, pady=5)

borrow_accept_button = tk.Button(window, text="Add book", font=("Roman", "11"),
                                 command=read_borrow)

choice_4 = tk.Button(window, text="Return a book", height=3, font=("Roman", "20"),
                     command=lib1.return_book)
choice_4.grid(row=9, column=0, rowspan=2, columnspan=6, sticky="nw", padx=5, pady=5)

exit_button = tk.Button(window, text="Exit", height=3, width=5, font=("Roman", "20"), command=window.destroy)
exit_button.grid(row=13, column=0, rowspan=2, columnspan=6, sticky="nw", padx=5, pady=5)

# ######################################################DISPLAY MENUS###################################################
welcome_msg = tk.Label(window, text=f'Welcome to our {lib1.name} library', font=("Roman", "35"), borderwidth=5,
                       relief="solid")
welcome_msg.grid(row=0, column=9, rowspan=2, columnspan=17, padx=10, pady=10, sticky='nw')

choice_prompt = tk.Label(window, text="Please select one of following options:", font=("Roman", "25"), borderwidth=5,
                         relief="solid")
choice_prompt.grid(row=3, column=0, columnspan=17, sticky="nw", padx=5, pady=5)


booklist = tk.Listbox(window, height=10, font=("Roman", "20"), borderwidth=5, relief="solid")
for books in lib1.all_books:
    booklist.insert(tk.END, books)
booklist_scroll = tk.Scrollbar(window, command=booklist.yview)
booklist.configure(yscrollcommand=booklist_scroll.set)


donate_label = tk.Label(window, text="Enter the name of the book you\n want to add:", font=("Roman", "11"))
donate_accept_label = tk.Label(window, text="Book added, thank you for your\n donation", font=("Roman", "11"))
donate_input = tk.Entry(window)

borrow_label = tk.Label(window, text="Please fill the borrrow form")
borrow_label_name = tk.Label(window, text="Name:")
borrow_label_book = tk.Label(window, text="Name of the book:")
borrow_input_name = tk.Entry(window)
borrow_input_book = tk.Entry(window)

window.title('User Interface')
# This needs to be at the end so that backgroudnd image is in the background
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
# bg_label.grid(row=0, column=0, rowspan=window.grid_size()[1], columnspan=window.grid_size()[0])
window.attributes('-fullscreen', True)
window.mainloop()
