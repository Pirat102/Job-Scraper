import re
import sys

hours = {
"12AM": "00",
"1AM": "01",
"2AM":	"02",
"3AM":	"03",
"4AM":	"04",
"5AM":	"05",
"6AM":	"06",
"7AM":	"07",
"8AM":	"08",
"9AM":	"09",
"10AM": "10",
"11AM": "11",
"12PM": "12",
"1PM":	"13",
"2PM":	"14",
"3PM":	"15",
"4PM":	"16",
"5PM":	"17",
"6PM":	"18",
"7PM":	"19",
"8PM":	"20",
"9PM":	"21",
"10PM": "22",
"11PM": "23"
}


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if valid := re.search(r"(1[0-2]|[1-9])(:[0-5][0-9])?\s(AM|PM)\sto\s(1[0-2]|[1-9])(:[0-5][0-9])?\s(AM|PM)", s, re.IGNORECASE):
        if valid.group(2):
            time_start = hours[(valid.group(1) + valid.group(3)).upper()] + valid.group(2) + " to "
        else:
            time_start = hours[(valid.group(1) + valid.group(3)).upper()] + ":00 to "
        if valid.group(5):
            time_end = hours[(valid.group(4) + valid.group(6)).upper()] + valid.group(5)
        else:
            time_end = hours[(valid.group(4) + valid.group(6)).upper()] + ":00"
    
    else:
        raise ValueError
    return time_start + time_end 
            
    
    
    



if __name__ == "__main__":
    main()