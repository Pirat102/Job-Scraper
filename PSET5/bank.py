

def main():
    x = input("Greeting: ").lower().strip()
    print(value(x))


def value(greeting):
    if greeting.split()[0].lower() == "hello" or greeting.split()[0].lower() == "hello,":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
