# Main logic in OOP aproach
import json


class Library:
    def __init__(self, name, all_books):
        self.name = name
        self.all_books = all_books
        self.borrowed = {}

    def check_booklist(self):
        print(f'Books available in {self.name} library:')
        for book in self.all_books:
            print(book)

    def add_book(self, book):
        if book in self.all_books:
            print(f'This book is already in {self.name} library')
        else:
            self.all_books.append(book)
            print(self.all_books)
            with open('owned_books.json', 'w') as f:
                json.dump(self.all_books, f)
                print(f'Book: {book} added to the list')

    def load_borrowed_db(self):
        borrowed_database = json.load(open('borrowed.json', 'r'))
        for borrow in borrowed_database:
            self.borrowed.update({str(list(borrow.keys()))[2:-2]: str(list(borrow.values()))[2:-2]})

    def write_to_json(self, lst, fn):
        with open(fn, 'w', encoding='utf-8') as file:
            file.write('[')
            for key, value in lst.items():
                if key != list(lst.keys())[-1]:
                    x = '{"' + key + '": "' + value + '"},'
                    file.write(x + '\n')
                else:
                    x = '{"' + key + '": "' + value + '"}'
                    file.write(x)
            file.write(']')

    def lend_book(self, name, book):
        self.load_borrowed_db()
        if book in self.all_books:
            if book not in self.borrowed:
                self.borrowed.update({book: name})
                self.write_to_json(self.borrowed, 'borrowed.json')
                print(f'{name} succesfully borrowed {book}')
            else:
                print(f'Book is already borrowed to {self.borrowed[name]}')
        else:
            print(f'Library {self.name} does not contain {book}')

    def return_book(self, name, book):
        self.load_borrowed_db()
        if (book, name) in self.borrowed.items():
            self.borrowed.pop(book)
            self.write_to_json(self.borrowed, 'borrowed.json')
            print(f'Succesfully returned {book} book, thank you {name}')
        elif book not in self.borrowed.keys():
            if name not in self.borrowed.values():
                print(f'Hi {name}, you did not borrow any book')
            elif book in self.all_books:
                print(f'We already have {book} back')
            else:
                print('Book is not in our db, try adding book instead')

        else:
            print('unexpected error')


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
                lib1.check_booklist()
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
    lib1 = Library('SampleLibrary1', books)
    main()
