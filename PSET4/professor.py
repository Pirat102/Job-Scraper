import random

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        if not guess(x, y, correct):
            print(f"{x} + {y} = {correct}")
        else:
            correct_answers += 1

    print(f"Score: {correct_answers}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def guess(x, y, correct):
    for attempt in range(3):
        try:
            user_input = int(input(f"{x} + {y} = "))
            if user_input == correct:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    return False

if __name__ == "__main__":
    main()
