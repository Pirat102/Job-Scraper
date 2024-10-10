
def main():
    x = input("Input: ")
    result = shorten(x)
    print(f"Output: {result}")


def shorten(word):
    vowels = ("aeiouAEIOU")
    filtered_chars = [char for char in word if char not in vowels]
    return "".join(filtered_chars)


if __name__ == "__main__":
    main()
