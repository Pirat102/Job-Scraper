import inflect
names = []
p = inflect.engine()
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break
result = p.join(names)
print("Adieu, adieu, to " + result)
