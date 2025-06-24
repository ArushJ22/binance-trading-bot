from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binance.vision/api'
        logging.info("SPOT Bot initialized with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }
            if order_type == ORDER_TYPE_LIMIT:
                params.update({
                    'price': price,
                    'timeInForce': TIME_IN_FORCE_GTC
                })

            order = self.client.create_order(**params)
            logging.info("Order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Order failed: %s", e)
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP_LOSS_LIMIT,
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info("Stop-Limit Order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Stop-Limit Order failed: %s", e)
            return None
