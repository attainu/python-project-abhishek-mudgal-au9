#!/usr/bin/python3

import json
import sys
import time

import requests
from tqdm import tqdm


# Globally available data, keys and api links

keys = {
    'IFTTT': 'jmcboACZjXX4kWcDwLslnxFe3a4_YzjIdZn4NjV5DrJ',
    'CRYPTO': '5ac61829f26de360f9d780fc892a0bbf'
}

api = {
    'IFTTT': 'https://maker.ifttt.com/trigger/{}/with/key/{}',
    'CRYPTO': 'https://api.nomics.com/v1/currencies/ticker?key={}&ids={}&convert={}'
}


class Crypto:

    # get price fetches the price and returns a float value
    # otherwise catches error and displays it to the user

    def get_price(self):
        json_url = api['CRYPTO'].format(keys['CRYPTO'],
            sys.argv[1], sys.argv[2])
        try:
            response = requests.get(json_url)
            return(float(response.json()[0]['price']))
        except requests.exceptions.RequestException:
            raise SystemExit("Please check your internet connection!")
        except json.decoder.JSONDecodeError:
            raise SystemExit("Market key invalid, please check or grab a new key!")

    # notify function uses IFTTT platform to send
    # notifications, post_data contains data to be posted on IFTTT Message

    def notify(self, channel, price):

        post_data = {
            'value1': sys.argv[1],
            'value2': "{} {}".format(price, sys.argv[2])
        }

        for i in tqdm(
            range(1),
            desc="Sending notification to {}".format(channel)
            ):
            trigger = api['IFTTT'].format(channel, keys['IFTTT']
            )
            requests.post(trigger, json=post_data)
            pass

    # Main Function checks the price, and calls
    # notification function.

    def main(self):
        while True:
            price = Crypto.get_price(self)
            print(price)
            if price > int(sys.argv[5]):
                Crypto.notify(self, sys.argv[4], price)
            time.sleep(int(sys.argv[3]))


if __name__ == "__main__":
    try:
        o = Crypto()
        o.main()
    except IndexError:
        raise SystemExit("""Usage: crypto-watch.py <CRYPTO> <CURRENCY> <PRICE INTERVAL> <CHANNEL> <TRIGGER>


        <CRYPTO> :              BTC, XMR, XRP, etc
        <CURRENCY>:             INR, USD, CAD, etc
        <PRICE INTERVAL>:       How and when price should be updated eg, 60 for 60 seconds.
        <CHANNEL>:              EG. telegram, twitter or any other applet which you have created.
        <TRIGGER>:              Trigger value, eg. 10000

        Use Ctrl+C to exit the program""")
