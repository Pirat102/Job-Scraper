## MM/DD/YYYY or September 8, 1636

months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}


def check(n):

    for l in n:
        if l == "/":
            n = n.split("/")
            numbers = True
            return numbers, n
        elif l == ",":
            n = n.replace(",","")
            n = n.split(" ")
            numbers = False
            return numbers, n
    else:
        None


while True:
    try:
        x = input("Date (MM/DD/YYYY): ").strip().title()
        numbers, n = check(x)


        if numbers and 0 < int(n[0]) <= 12 and 0 < int(n[1]) <= 31:
            print(f"{int(n[2])}-{int(n[0]):02}-{int(n[1]):02}")
            break
        else:
            if n[0] in months and int(n[1]) <= 31:
                print(f"{int(n[2])}-{months[n[0]]}-{int(n[1]):02}")
                break
    except KeyError:
        continue
    except ValueError:
        continue
    except TypeError:
        continue





