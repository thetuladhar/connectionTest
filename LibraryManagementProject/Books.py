
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def display(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Quantity: {self.quantity}")
        print("----------------------------")

    def add_book(self, quantity_to_add):
        if quantity_to_add > 0:
            self.quantity += quantity_to_add
            print(f"Added {quantity_to_add} copies of '{self.title}'. New quantity: {self.quantity}")
        else:
            print("Invalid quantity to add. Quantity must be greater than 0.")

    def remove_book(self, quantity_to_remove):
        if quantity_to_remove > 0:
            if self.quantity >= quantity_to_remove:
                self.quantity -= quantity_to_remove
                print(f"Removed {quantity_to_remove} copies of '{self.title}'. New quantity: {self.quantity}")
            else:
                print(f"Error: Not enough copies of '{self.title}' to remove.")
        else:
            print("Invalid quantity to remove. Quantity must be greater than 0")
# Class for borrowers