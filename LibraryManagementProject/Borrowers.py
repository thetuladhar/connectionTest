import csv 

class Borrower:
    def __init__(self, borrower_id, name, contact):
        self.borrower_id = borrower_id
        self.name = name
        self.contact = contact

    def display(self):

        print(f"Borrower ID: {self.borrower_id}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print("----------------------------")

    def save_to_csv(self, file_path):
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.borrower_id, self.name, self.contact])

    @classmethod
    def load_from_csv(cls, file_path):
        borrowers = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                borrower = cls(int(row[0]), row[1], row[2])
                borrowers.append(borrower)
        return borrowers