import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate_1st_attempt(ip):
    if re.search(r"^(25[0-5]|2[0-4][0-9]|[0-9][0-9]?|1[0-9]?[0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-9][0-9]?|1[0-9]?[0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-9][0-9]?|1[0-9]?[0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-9][0-9]?|1[0-9]?[0-9]?)$", ip):
        return True
    else:
        return False

def validate(ip):
    valid = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)"
    pattern = rf"^{valid}\.{valid}\.{valid}\.{valid}$"
    
    if re.fullmatch(pattern, ip):
        return True
    else:
        return False
    


if __name__ == "__main__":
    main()
    
