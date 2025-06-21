from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)         # Uses __str__
    print(repr(my_book))   # Uses __repr__

    del my_book            # Calls __del__

if __name__ == "__main__":
    main()
