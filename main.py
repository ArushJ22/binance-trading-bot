import logging
from config import API_KEY, API_SECRET
from bot import BasicBot
from utils import validate_order_input, validate_stop_limit
import questionary

logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    print("Welcome to the Binance Futures Testnet Trading Bot")

    symbol = questionary.text("Enter symbol (e.g., BTCUSDT):").ask().upper()
    side = questionary.select(
        "Select side:", choices=["BUY", "SELL"]
    ).ask().upper()
    order_type = questionary.select(
        "Select order type:", choices=["MARKET", "LIMIT", "STOP_LIMIT"]
    ).ask().upper()
    quantity = float(questionary.text("Enter quantity:").ask())

    if order_type == "STOP_LIMIT":
        stop_price = float(questionary.text("Enter stop price:").ask())
        limit_price = float(questionary.text("Enter limit price:").ask())
        try:
            validate_stop_limit(symbol, side, quantity, stop_price, limit_price)
            order = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
            if order:
                print("Stop-Limit Order placed successfully!")
                print(order)
            else:
                print("Failed to place Stop-Limit order.")
        except AssertionError as e:
            print(f"Input Error: {e}")

    else:
        price = None
        if order_type == "LIMIT":
            price = float(questionary.text("Enter price:").ask())
        try:
            validate_order_input(symbol, side, order_type, quantity, price)
            order = bot.place_order(symbol, side, order_type, quantity, price)
            if order:
                print("Order placed successfully!")
                print(order)
            else:
                print("Failed to place order. Check logs.")
        except AssertionError as e:
            print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
