def main():
    x = input("Input your emoji: ")
    convert(x)

def convert(user_str):
    print(user_str.replace(":)", "🙂").replace(":(", "🙁"))


main()
