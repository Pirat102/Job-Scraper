def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # Check if the length of the plate is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if all characters are letters or numbers
    if not s.isalnum():
        return False

    # Check if the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Check that there is at least one letter before any number
    found_number = False
    for char in s:
        if char.isdigit():
            found_number = True
            break
    if found_number:
        if any(char.isalpha() for char in s[s.index(char):]):
            return False

    # Check that the first number is not '0'
    if any(char.isdigit() for char in s) and s[s.index(next(filter(str.isdigit, s)))] == '0':
        return False

    return True


main()
