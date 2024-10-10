from datetime import date
import inflect
import sys


def main():
    try:
        birthday = input("Date of Birth: ").split("-")
        minutes = calculate_minutes(birthday)
    except:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birthday)
    words = convert(minutes)
    print(f"{words[0].capitalize()}{words[1:]} minutes")

    

def calculate_minutes(birthday):
    y, m, d = birthday
    today = date.today()
    birth = date(int(y), int(m), int(d))
    days_diff = (today - birth)
    return days_diff.days * 24 * 60
    
    
    
def convert(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="") # type: ignore
    return words
    











if __name__ == "__main__":
    main()
