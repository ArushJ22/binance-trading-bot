from binance.client import Client
from config import API_KEY, API_SECRET

def test_connection():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    try:
        account_info = client.futures_account()
        print("Connected to Binance Futures Testnet!")
        print(f"Total USDT Balance: {account_info['totalWalletBalance']}")
    except Exception as e:
        print("Connection failed!")
        print(e)

if __name__ == "__main__":
    test_connection()
