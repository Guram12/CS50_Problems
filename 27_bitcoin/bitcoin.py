import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("command-line argument is not a number")
    data = request.json()
    price = data["bpi"]["USD"]["rate"]
    price = price.replace(",","")
    print(f"${float(price) * float(sys.argv[1]):,.4f}")






















