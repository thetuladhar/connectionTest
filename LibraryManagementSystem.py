

class Books:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

class Borrowers:
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id

class Transactions:
    def __init__(self, book, borrower, borrowed_date):
        self.book = book
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.returned_date = None