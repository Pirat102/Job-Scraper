import re


def main():
    print(parse(input("HTML: ")))



def parse(s):
    if src := re.search(r'youtube\.com/embed/(.+?)"', s):
        return ("https://youtu.be/" + src.group(1))
    

if __name__ == "__main__":
    main()