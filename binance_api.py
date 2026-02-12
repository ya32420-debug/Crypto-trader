import requests
import time

class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.binance.com'

    def get_account(self):
        url = f"{self.base_url}/api/v3/account"
        headers = {
            'X-MBX-APIKEY': self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_price(self, symbol):
        url = f"{self.base_url}/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        return response.json()

    # Add more methods for other Binance API endpoints

# Example Usage:
# api = BinanceAPI('your_api_key', 'your_api_secret')
# print(api.get_account())
# print(api.get_price('BTCUSDT'))