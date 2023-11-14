import csv
from Books import Book
# Class for managing the catalog of books
class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return
        print("Book not found.")

    def update_book_quantity(self, book_id, quantity):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity = quantity
                return
        print("Book not found.")

    def display_books(self):
        for book in self.books:
            book.display()

    def save_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Title", "Author", "Quantity"])
            for book in self.books:
                writer.writerow([book.book_id, book.title, book.author, book.quantity])

    def load_from_csv(self, file_path):
        self.books = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(int(row["Book ID"]), row["Title"], row["Author"], int(row["Quantity"]))
                self.books.append(book)