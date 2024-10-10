def main():

    camel_case = input("camelCase: ")

    snake_case = convert(camel_case)

    print(snake_case)

def convert(x):
    snake_case = ""
    for l in x:
        if l.isupper():
            snake_case += "_" + l.lower()
        else:
            snake_case += l

    return snake_case


main()
        