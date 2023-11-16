import csv
# Class for transactions
class Transaction:
    def __init__(self, transaction_id, book, borrower, borrowed_date, expected_return_date, actual_return_date=""):
        self.transaction_id = transaction_id
        self.book = book
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.expected_return_date = expected_return_date
        self.actual_return_date = actual_return_date

    def display(self):
        print(f"Transaction ID: {self.transaction_id}")
        print("Book Information:")
        self.book.display()
        print("Borrower Information:")
        self.borrower.display()
        print(f"Borrowed Date: {self.borrowed_date}")
        print(f"Expected Return Date: {self.expected_return_date}")
        print(f"Actual Return Date: {self.actual_return_date}")

    def save_to_csv(self, file_path):
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.transaction_id, self.book.book_id, self.borrower.borrower_id, self.borrowed_date, self.expected_return_date, self.actual_return_date])

    @classmethod
    def load_from_csv(cls, file_path, books, borrowers):
        transactions = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                book_id = int(row[1])
                borrower_id = int(row[2])
                book = next((b for b in books if b.book_id == book_id), None)
                borrower = next((b for b in borrowers if b.borrower_id == borrower_id), None)
                #borrower = next((b for b in borrowers if borrower.borrower_id == borrower_id), None)#was
                transaction = cls(int(row[0]), book, borrower, row[3], row[4], row[5])
                transactions.append(transaction)
        return transactions