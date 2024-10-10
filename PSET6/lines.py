import sys
import os


def main():
    validate_input()
    path = sys.argv[1]
    print(number_of_lines(path))

def validate_input():
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
        

    
    

def number_of_lines(path):
    lines = []
    try:
        with open(path) as file:
            for line in file:
                if line.strip() == "" or line.strip()[0] == "#":
                    continue
                else:
                    lines.append(line.strip())
            return len(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
