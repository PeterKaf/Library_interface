import json
from PIL import Image, ImageTk
import tkinter as tk
import Classes

db_name = "owned_books.json"
book_database = json.load(open(db_name, 'r'))
lib1 = Classes.Library('SampleLibrary1', book_database)

window = tk.Tk()

canvas = tk.Canvas(window, width=1920, height=1080)
canvas.pack()
# ########################################################TRACKERS######################################################
is_but1_on = False
is_but2_on = False
is_but3_on = False
is_but4_on = False

is_anybutton_on = False
# #########################################################CANVAS#######################################################
donatebox_canvas = tk.Canvas(window, width=310, height=200, borderwidth=5, relief="solid")
borrowbox_canvas = tk.Canvas(window, width=310, height=200, borderwidth=5, relief="solid")

# ########################################################FUNCTIONS#####################################################


def button1_switch():
    global is_but1_on, is_but2_on
    if is_but1_on:
        booklist.place_forget()
        is_but1_on = False
    else:
        if is_but2_on:
            donatebox_canvas.place_forget()
            donate_label.place_forget()
            donate_accept_label.place_forget()
            donate_accept_button.place_forget()
            is_but2_on = False
        booklist.place(anchor="nw", x=600, y=250)
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
    global is_but2_on, is_but1_on, donate_input
    if is_but2_on:
        donatebox_canvas.place_forget()
        donate_label.place_forget()
        donate_accept_label.place_forget()
        donate_accept_button.place_forget()
        is_but2_on = False
    else:
        if is_but1_on:
            booklist.place_forget()
            is_but1_on = False
        donatebox_canvas.place(anchor="nw", x=700, y=250)
        donatebox_canvas.create_window(110, 100, window=donate_input, width=200)
        donate_label.place(anchor="nw", x=720, y=280)
        donate_accept_button.place(anchor="nw", x=913, y=335)
        is_but2_on = True


def read_donate():
    global donate_input
    x = donate_input.get()
    lib1.add_book(x)
    donate_accept_label.place(anchor="nw", x=720, y=380)


def button3_switch():
    global is_but3_on, borrow_input_name, borrow_input_book
    if is_but3_on:
        borrowbox_canvas.place_forget()
        borrow_label.place_forget()
        borrow_label_name.place_forget()
        borrow_label_book.place_forget()
        borrow_accept_button.place_forget()
        is_but3_on = False
    else:
        borrowbox_canvas.place(anchor="nw", x=700, y=250)
        borrowbox_canvas.create_window(110, 100, window=borrow_input_name, width=200)
        borrowbox_canvas.create_window(110, 150, window=borrow_input_book, width=200)
        borrow_label.place(anchor="nw", x=720, y=280)
        borrow_label_name.place(anchor="nw", x=720, y=320)
        borrow_label_book.place(anchor="nw", x=720, y=365)
        borrow_accept_button.place(anchor="nw", x=913, y=358.5)
        is_but3_on = True


def read_borrow():
    global borrow_input_name, borrow_input_book
    x = borrow_input_name.get()
    y = borrow_input_book.get()
    lib1.add_book(x)
    donate_accept_label.place(anchor="nw", x=720, y=380)


# ######################################################CHOICE BUTTONS##################################################

choice_1 = tk.Button(window, text="Display books in our stock", height=3, font=("Roman", "20"),
                     command=lambda: button1_switch())
choice_1.place(anchor="nw", y=250)

choice_2 = tk.Button(window, text="Donate a book", height=3, font=("Roman", "20"),
                     command=lambda: button2_switch())
choice_2.place(anchor="nw", y=400)

donate_accept_button = tk.Button(window, text="Add book", font=("Roman", "11"),
                                 command=read_donate)

choice_3 = tk.Button(window, text="Borrow a book", height=3, font=("Roman", "20"),
                     command=lambda: button3_switch())
choice_3.place(anchor="nw", y=550)

borrow_accept_button = tk.Button(window, text="Add book", font=("Roman", "11"),
                                 command=read_borrow)

choice_4 = tk.Button(window, text="Return a book", height=3, font=("Roman", "20"),
                     command=lib1.return_book)
choice_4.place(anchor="nw", y=700)

exit_button = tk.Button(window, text="Exit", height=3, width=5, font=("Roman", "20"), command=window.destroy)
exit_button.place(anchor="nw", y=850)

# ######################################################DISPLAY MENUS###################################################
welcome_msg = tk.Label(window, text=f'Welcome to our {lib1.name} library', font=("Roman", "35"), borderwidth=5,
                       relief="solid")
welcome_msg.place(anchor="center", x=960, y=75)

choice_prompt = tk.Label(window, text="Please select one of following options:", font=("Roman", "25"), borderwidth=5,
                         relief="solid")
choice_prompt.place(anchor="nw", y=150)

booklist = tk.Label(window, text=formatted_booklist(book_database), height=len(book_database), font=("Roman", "20"),
                    borderwidth=5, relief="solid")
donate_label = tk.Label(window, text="Enter the name of the book you\n want to add:", font=("Roman", "11"))
donate_accept_label = tk.Label(window, text="Book added, thank you for your\n donation", font=("Roman", "11"))
donate_input = tk.Entry(window)

borrow_label = tk.Label(window, text="Please fill the borrrow form")
borrow_label_name = tk.Label(window, text="Name:")
borrow_label_book = tk.Label(window, text="Name of the book:")
borrow_input_name = tk.Entry(window)
borrow_input_book = tk.Entry(window)

window.title('User Interface')
window.geometry("1920x1080")
bgImage = ImageTk.PhotoImage(Image.open("Background.jpg"))
bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

window.mainloop()
