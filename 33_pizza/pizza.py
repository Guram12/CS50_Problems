import sys
from tabulate import tabulate
import csv

arguments = sys.argv

def main():
    if len(arguments) != 2:
        sys.exit("Please provide the path to a single CSV file as a command-line argument.")

    file_path = arguments[1]
    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file.")

    try:
        file_contents = read_file(file_path)
        t_file = tabulate(file_contents, headers="firstrow" , tablefmt = "grid")
        print(t_file)
    except FileNotFoundError:
        sys.exit("File not found.")

def read_file(file_path):
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        return list(csv_reader)

if __name__ == "__main__":
    main()

