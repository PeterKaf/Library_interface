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
