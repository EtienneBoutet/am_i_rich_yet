# am_i_rich_yet
Python script to estimate the value (CAD) of a LTC wallet. This script may stop working if the APIs change anything in their data or simply if they stop working. I also don't know how much time it takes for the APIs to refresh their data.

Étienne Boutet - 2017

### Usage

To use this script you will need to have Python 3 or + on your computer. You will need to add your address in the LTC_ADDRESS constant (Line 6).

### Library

I used the Requests library to fetch data from 3 APIs.

Requests = http://docs.python-requests.org/en/master/

### APIs

I used chain.so API to get the amount of LTC in a wallet.

https://chain.so/api

I also used coinmarketcap.com API to get the value in USD of a single LTC.

https://coinmarketcap.com/api/

Finally, I used api.fixer.io to get the exchange rate of CAD vs USD.

http://fixer.io
