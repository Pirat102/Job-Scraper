def convert():
    while True:

        try:
            n = input("Fraction: ").split("/")
            x, y = int(n[0]), int(n[1])
            result = round(x/y * 100)
            if x > y:
                continue
            break

        except ZeroDivisionError:
            print("the number can't be 0")
        except ValueError:
            print("It must be an integer")

    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")


convert()

