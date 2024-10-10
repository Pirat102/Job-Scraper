def main():
    exp = input("Expression: ").strip().split()
    result = calculate(exp)
    print(f"{result:.1f}")



def calculate(exp):
    operator = exp[1]
    num1 = int(exp[0])
    num2 = int(exp[2])
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        operator == "/"
        return num1 / num2

main()
