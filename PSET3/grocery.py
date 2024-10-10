groceries = {}

while True:
    try:
        x = input("").upper()
        if x in groceries:
            groceries[x] += 1
        else:
            groceries[x] = 1


    except EOFError:
        for k, v in sorted(groceries.items()):
            print(v, k)
        break


