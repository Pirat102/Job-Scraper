x = input("Greeting: ").lower().strip()
if x.split()[0] == "hello" or x.split()[0] == "hello,":
    print("$0")
elif x[0] == "h":
    print("$20")
else:
    print("$100")



