import requests
import sys

try:
    x = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")


try:
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(URL)
except requests.RequestException:
    print("Invalid")


o = response.json()

rate = o["bpi"]["USD"]["rate_float"]

price = x * rate
print(f"${price:,.4f}")

