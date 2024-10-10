import random

while True:
    try:
        x = int(input("Level: "))
        random_number = random.randint(1, x)
        break

    except Exception as e:
        continue


def guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            elif guess == random_number:
                print("Just right!")
                break
        except Exception as e:
            continue

guess()
