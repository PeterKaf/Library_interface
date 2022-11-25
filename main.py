# Main logic in OOP aproach
import json
import Classes


def main():
    while True:
        print(f'Welcome to {lib1.name}. Please select action you want to take')
        selection = """
        1.Display booklist
        2.Add book to booklist
        3.Borrow book
        4.Return book
        """
        user_action = input("Press q to quit or press c to continue")
        if user_action == 'q':
            break
        elif user_action == 'c':
            print(selection)
            choice = input('Select 1-4 from the menu')
            if choice == '1':
                print(lib1.check_booklist())
            elif choice == '2':
                book = str(input('Specify name of the book you want to add:'))
                lib1.add_book(book)
            elif choice == '3':
                name = input('What is your name?')
                book = input('What book you want to borrow?')
                lib1.lend_book(name, book)
            elif choice == '4':
                name = input('What is your name?')
                book = input('What book you want to return?')
                lib1.return_book(name, book)
            else:
                print('Select a number 1-4 according to the menu')
        else:
            print('Please enter valid option')


if __name__ == '__main__':
    books = []
    db_name = "owned_books.json"
    book_database = json.load(open(db_name, 'r'))
    for b in book_database:
        books.append(b)
    lib1 = Classes.Library('SampleLibrary1', books)
    main()
