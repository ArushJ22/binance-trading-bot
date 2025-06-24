def validate_order_input(symbol, side, order_type, quantity, price=None):
    assert side in ["BUY", "SELL"], "Invalid side"
    assert order_type in ["MARKET", "LIMIT", "STOP_LIMIT"], "Invalid order type"
    assert quantity > 0, "Quantity must be positive"
    if order_type == "LIMIT":
        assert price is not None and price > 0, "Limit price required"

def validate_stop_limit(symbol, side, quantity, stop_price, limit_price):
    assert side in ["BUY", "SELL"], "Invalid side"
    assert quantity > 0, "Quantity must be positive"
    assert stop_price > 0, "Stop price must be positive"
    assert limit_price > 0, "Limit price must be positive"
