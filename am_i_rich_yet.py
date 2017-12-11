import requests
import os

# Data gathering

LTC_ADDRESS = '' ## <--- Your wallet adress goes there

api_wallet_adress = requests.get('https://chain.so/api/v2/get_address_balance/LTC/' + LTC_ADDRESS).json()
ltc_amount = float(api_wallet_adress['data']['confirmed_balance'])
json_ltc = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/').json()
ltc_usd_price = float(json_ltc[0]["price_usd"])
json_exchange_rate = requests.get('https://api.fixer.io/latest?base=USD').json()
exchange_rate = float(json_exchange_rate["rates"]['CAD'])
wallet_usd_price = ltc_amount * ltc_usd_price

# Data display

os.system('clear')
print("Litecoin (LTC) - Value")
print("=================================================\n")
print("LTC value (USD) is :", ltc_usd_price)
print("You have :", ltc_amount, "LTCs")
# Weird formating for the ,xx. Sorry.
print("Your wallet is worth :", "{0:.2f}".format(round(wallet_usd_price * exchange_rate,2)), "CAD")

input()
