
def automat():
    cents = [25, 10, 5]
    amount_due = 50

    while True:
        x = int(input(f"Amount Due: {amount_due}\nInsert amount: "))
        if x in cents:
            amount_due -= x
        if amount_due <=0:
            print(f"Change Owed: {-amount_due}")
            break

automat()
