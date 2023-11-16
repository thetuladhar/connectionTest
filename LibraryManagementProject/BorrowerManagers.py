import csv
from Borrowers import Borrower

# Class for managing borrowers
class BorrowerManager:
    def __init__(self):
        self.borrowers = []

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def remove_borrower(self, borrower_id):
        for borrower in self.borrowers:
            if borrower.borrower_id == borrower_id:
                self.borrowers.remove(borrower)
                return
        print("Borrower not found.")

    def update_borrower(self, borrower_id, name, contact):
        for borrower in self.borrowers:
            if borrower.borrower_id == borrower_id:
                borrower.name = name
                borrower.contact = contact
                return
        print("Borrower not found.")

    def display_borrowers(self):
        for borrower in self.borrowers:
            borrower.display()

    def save_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Borrower_ID", "Name", "Contact"])
            for borrower in self.borrowers:
                writer.writerow([borrower.borrower_id, borrower.name, borrower.contact])

    def load_from_csv(self, file_path):
        self.borrowers = Borrower.load_from_csv(file_path)