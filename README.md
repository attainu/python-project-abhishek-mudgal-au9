# **Crypto Watch**

## About

Crypto Watch (`crypto-watch`) is a simple python program which notifies user if their desired crypto currency has crossed a certain threshold using IFTTT Notification API.
Market Data from https://api.nomics.com
Notification Service https://ifttt.com
Libraries used: `tqdm`, `json`, `requests`, `time`


## Installation
Installation is fairly simple and straight forward

    pip3 install requests tqdm
    git clone https://github.com/attainu/python-project-abhishek-mudgal-au9 -b dev ~/crypto-watch
     
   ##  Running the Script
  You can run the app either on a hosted server or on your local machine.

### Usage Syntax
Before using the program, get your market keys from [here](https://api.nomics.com) and your IFTTT keys from [here](https://ifttt.com).

    cd ~/crypto-watch
    ./crypto-watch CRYPTO CURRENCY INTERVAL CHANNEL THRESHOLD
	
##### CRYPTO
Crypto Watch program supports multiple crypto currencies, use their ticker code. Eg, BTC for Bitcoin, XMR for Monero, XRP for Ripple. Get the complete list from [here](https://nomics.com/).

##### CURRENCY
API supports major currencies you would like to have price of crypto currency in. Eg, INR for Indian Rupee, USD for US Dollar, CAD for Canadian Dollar and etc.

##### INTERVAL
Crypto Watch needs time(seconds) as an argument to fetch the updated price.

##### CHANNEL
You can use multiple channels through which you can receive price. Eg, telegram for Telegram, twitter for Twitter, SMS for Short message on your number.
Instructions:

 1. Download IFTTT app from the respective store.
 2. Install applets Twitter https://ifttt.com/applets/ZdeyxC8p , Telegram https://ifttt.com/applets/zCXiNvbz
 3. [Optional] You can also create your new applets on https://ifttt.com . Applet>Webhooks>{Your Notification Service}>Compose message>Use $VALUE1 for Crypto code and $VALUE2 for the price!

##### THRESHOLD
Program requires an threshold value to compare price. If the fetch priced has gone beyond threshold, a notification will be sent!

## Example

    ./crypto-watch.py BTC USD 60 telegram 10000

## License

[GPLv3](https://github.com/attainu/python-project-abhishek-mudgal-au9/blob/dev/LICENSE)

