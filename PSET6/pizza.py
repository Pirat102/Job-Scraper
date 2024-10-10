import sys
from tabulate import tabulate

def main():
    validate_input()
    path = sys.argv[1]
    file_type = check_file(path)
    drawing(file_type)

def validate_input():
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
              
def check_file(path):
    try:
        with open(path) as file:
            return path
            
    except FileNotFoundError:
        sys.exit("File does not exist")

def drawing(file_type):
    table = []
    with open(file_type) as file:
        for row in file:
            table.append(row.strip().split(","))
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
