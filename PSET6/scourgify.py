import sys
import csv

def main():
    validate_input()
    old_file, new_file = sys.argv[1], sys.argv[2]
    data = students_data(old_file)
    create_file(new_file, data)



def validate_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few line arguments")
    elif sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
        sys.exit("Not a CSV file")
              
              
def students_data(old_file):
    students = []
    try:
        with open(old_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_elements = row["name"].split(",")
                last, first = name_elements[0], name_elements[1].strip()
                students.append({"first": first, "last": last, "house": row["house"]})
        return students
    except FileNotFoundError:
        sys.exit("File does not exist")
        


def create_file(file_name, data):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)
        
        
            
        
if __name__ == "__main__":
    main()