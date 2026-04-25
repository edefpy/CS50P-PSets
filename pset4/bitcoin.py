import sys
import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        amount = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=3897554ec6809e6b4ed557466365fbfc289187466ed9dab4599ab5de4c324e23"
        )
    except requests.RequestException:
        print("API request failed")
    else:
        btc_infos = response.json()
        usd_price = float(btc_infos["data"].get("priceUsd")) * amount
        print(f"${usd_price:,.4f}")


main()
