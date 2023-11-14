#Import Library
import os
import csv
from datetime import datetime,timedelta

#Import from other files
from CreateCSV import create_csv
from Books import Book
from Borrowers import Borrower
from Transactions import Transaction
from BookCatalogs import BookCatalog
from BorrowerManagers import BorrowerManager

# Class for managing transactions
class TransactionManager:
    def __init__(self, books, borrowers):
        self.transactions = []
        self.books = books
        self.borrowers = borrowers

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_transactions(self):
        for transaction in self.transactions:
            transaction.display()

    def save_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Transaction ID", "Book ID", "Borrower_ID", "Borrowed Date", "Expected Return Date", "Actual Return Date"])
            for transaction in self.transactions:
                writer.writerow([transaction.transaction_id, transaction.book.book_id, transaction.borrower.borrower_id, transaction.borrowed_date, transaction.expected_return_date, transaction.actual_return_date])

    def load_from_csv(self, file_path):
        self.transactions = Transaction.load_from_csv(file_path, self.books, self.borrowers)

# Command-line interface (CLI)
def main():
    book_catalog = BookCatalog()
    borrower_manager = BorrowerManager()
    books_file = "books.csv"
    borrowers_file = "borrowers.csv"
    transactions_file = "transactions.csv"

    # Load data from CSV files
    book_catalog.load_from_csv(books_file)
    borrower_manager.load_from_csv(borrowers_file)
    transaction_manager = TransactionManager(book_catalog.books, borrower_manager.borrowers)
    transaction_manager.load_from_csv(transactions_file)

    while True:
        #DISPLAY OPTIONS
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book Quantity")
        print("-----------------------------")
        print("4. Add Borrower")
        print("5. Remove Borrower")
        print("6. Update Borrower Information")
        print("-----------------------------")
        print("7. Display Books")
        print("8. Display Borrowers")
        print("-----------------------------")
        print("9. Borrow Book")
        print("10. Return Book")
        print("-----------------------------")
        print("0. Exit")

        #GET INPUT FROM USER
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Book
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            book = Book(book_id, title, author, quantity)
            book_catalog.add_book(book)

            # Save the data to CSV file
            book_catalog.save_to_csv(books_file)



        elif choice == "2":
            # Remove Book
            book_id = int(input("Enter Book ID to remove: "))
            book_catalog.remove_book(book_id)

             # Save the data to CSV file
            book_catalog.save_to_csv(books_file)


        elif choice == "3":
            # Update Book Quantity
            book_id = int(input("Enter Book ID to update quantity: "))
            quantity = int(input("Enter new quantity: "))
            book_catalog.update_book_quantity(book_id, quantity)

             # Save the data to CSV file
            book_catalog.save_to_csv(books_file)


        elif choice == "4":
            # Add Borrower
            borrower_id = int(input("Enter Borrower ID: "))
            name = input("Enter Name: ")
            contact = input("Enter Contact: ")
            borrower = Borrower(borrower_id, name, contact)
            borrower_manager.add_borrower(borrower)
            # Save the data to CSV file
            borrower_manager.save_to_csv(borrowers_file)

        elif choice == "5":
            # Remove Borrower
            borrower_id = int(input("Enter Borrower ID to remove: "))
            borrower_manager.remove_borrower(borrower_id)
            # Save the data to CSV file
            borrower_manager.save_to_csv(borrowers_file)

        elif choice == "6":
            # Update Borrower Information
            borrower_id = int(input("Enter Borrower ID to update information: "))
            name = input("Enter new Name: ")
            contact = input("Enter new Contact: ")
            borrower_manager.update_borrower(borrower_id, name, contact)



        elif choice == "7":
            # Display Books
            print(" _______________________________")
            print("|DISPLAYING BOOKS IN THE LIBRARY|")
            print(" _______________________________")
            book_catalog.display_books()
            print("---------------------------------------")

        elif choice == "8":
            # Display Borrowers
            print(" _______________________________")
            print(" |    DISPLAYING BORROWERS      |")
            print (" _______________________________")
            borrower_manager.display_borrowers()
            print("---------------------------------------")


        elif choice == "9":
            # Borrow Book
            book_id = int(input("Enter Book ID to borrow: "))
            borrower_id = int(input("Enter Borrower ID: "))
            # Check if the book is available
            for book in book_catalog.books:
                if book.book_id == book_id:
                    if book.quantity > 0:
                        borrowed_date = datetime.now().strftime("%Y-%m-%d")
                        expected_return_date = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")

                        transaction_id = len(transaction_manager.transactions) + 1
                        transaction = Transaction(transaction_id, book, borrower_manager.borrowers[borrower_id - 1], borrowed_date, expected_return_date, "")
                        transaction_manager.add_transaction(transaction)
                        book.quantity -= 1
                    else:
                        print("Book OUT of stock. SORRY .NOT available for borrowing.")
                    break
            else:
                print("Book not found. Try Again!")

            # Save the data to CSV files
            book_catalog.save_to_csv(books_file)
            borrower_manager.save_to_csv(borrowers_file)
            transaction_manager.save_to_csv(transactions_file)

        elif choice == "10":
            # Return Book
            transaction_id = int(input("Enter Transaction ID to return the book: "))
            for transaction in transaction_manager.transactions:
                if transaction.transaction_id == transaction_id:
                    actual_return_date = datetime.now().strftime("%Y-%m-%d")
                    transaction.actual_return_date = actual_return_date
                    # Increase the book quantity when returned
                    transaction.book.quantity += 1
                    break
            else:
                print("Transaction not found.")

            # Save the data to CSV files
            book_catalog.save_to_csv(books_file)
            borrower_manager.save_to_csv(borrowers_file)
            transaction_manager.save_to_csv(transactions_file)

        elif choice == "0":
            # Save the data to CSV files and exit
            book_catalog.save_to_csv(books_file)
            borrower_manager.save_to_csv(borrowers_file)
            transaction_manager.save_to_csv(transactions_file)
            print("Thank You and Goodbye!")
            break
if __name__ == "__main__":
    main()