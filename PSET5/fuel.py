
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge(percentage)



def convert(fraction):
    fraction.split("/")
    x, y = fraction[0], fraction[2]

    if y == "0":
        print(y)
        raise ZeroDivisionError

    elif int(x) > int(y):
        raise ValueError

    else:
        result = round(int(x) / int(y) * 100)
        return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()



