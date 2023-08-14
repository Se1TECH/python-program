# python program to a simple library management system
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower = None
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        book = Book(title, author)
        self.books.append(book)
        print("Book Append Successfully")

    def lend_book(self):
        if not self.books:
            print("No Books Available.")
        else:
            self.display_books()
            book_index = int(input("Enter Index of book to lend: "))
            if 0<= book_index < len(self.books):
                book = self.books[book_index]
                if book.is_available:
                    borrower = input("Enter Borrower name: ")
                    book.is_available = False
                    book.borrower = borrower
                    print(f"Book '{book.title}' lent to {borrower}")
                else:
                    print("Book is already lent.")
            else:
                print("Invalid book index.")

    def display_books(self):
        if not self.books:
            print("No Books Available.")
        else:
            print("\n---- Library Books ----")
            for index,book in enumerate(self.books):
                availability = "Available" if book.is_available else "Lent to " + book.borrower 
                print(f"[{index}] '{book.title}' by {book.author} - {availability}")

    def return_book(self):
        if not self.books:
            print("No books available.")
        else:
            self.display_books()
            book_index = int(input("Enter the index of book to return: "))
            if 0 <= book_index < len(self.books):
                book = self.books[book_index]
                if not book.is_available:
                    book.is_available = True
                    borrower = book.borrower
                    book.borrower = None
                    print(f"Book '{book.title}' returned by {borrower}. ")
                else:
                    print("Book is already available")
            else:
                print("Invalid Book Index.")

# Creating library
library = Library()

# Menu loop
while True:
    print("\n\n---- Library Management System ----")
    print("1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter Your Choice[1-5]: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.lend_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.display_books()
    elif choice == "5":
        print("\nYou are exiting")
        break
    else:
        print("invalid Choice. please try again")
    





