#Import Library
import os
import csv

# FUNCTION TO CREATE CSV file if it does not already exists
def create_csv(filename, columns):
    # Check if the file already exists
    if not os.path.isfile(filename):
        # Initialize the CSV file and write the header row
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
        print(f"CSV file '{filename}' created.")
    else:
        print(f"CSV file '{filename}' already exists. Not creating a new one.")

create_csv("books.csv",["Book ID","Title","Author","Quantity"])
create_csv("borrowers.csv",["Borrower_ID", "Name", "Contact"])
create_csv("transactions.csv",["Transaction ID", "Book ID", "Borrower_ID",
                               "Borrowed Date", "Expected Return Date", "Actual Return Date"])
