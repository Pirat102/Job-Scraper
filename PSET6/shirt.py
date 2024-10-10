from PIL import Image, ImageOps
import sys, os

def main():
    old, new = validate_input()
    create_image(old, new)
    

def validate_input():
    extensions = [".jpg", ".png", ".jpeg"]
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few line arguments")
    else:
        old, new = sys.argv[1], sys.argv[2]
        old_end = os.path.splitext(old)[1]
        new_end = os.path.splitext(new)[1]
        if old_end not in extensions or new_end not in extensions:
            sys.exit("Invalid input")
        elif old_end != new_end:
            sys.exit("Input and output have different extensions")
    return old, new


def create_image(old, new):
    shirt = Image.open("shirt.png")
    try:
        img = Image.open(old)
    except FileNotFoundError:
        sys.exit("File does not exist")
    size = shirt.size
    
    resize = ImageOps.fit(img, size)
    resize.paste(shirt, shirt)
    resize.save(new)



if __name__ == "__main__":
    main()


        



