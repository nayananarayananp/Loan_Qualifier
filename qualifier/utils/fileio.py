""" Helper function to load csv data. """

import csv


def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, qualifying_loans):
    
    # Create a `csvwriter` using the `csv` library. Use the csv library and `csv.writer` to write the header row
    # and each row of `loan.values()` from the `qualifying_loans` list.
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    # Use `with open` to open a new CSV file. Output this list of qualifying loans to a csv file
    with open(csvpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for loan in qualifying_loans:
            writer.writerow(loan)