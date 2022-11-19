from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = 'PKWF88ZVMO01Z9RM8FL8'
SECRET_KEY = 'Ff9vN4vkdkRS6vi9koeWLThFryFKpq1rr0iMQgye'

# trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# market_order_data = MarketOrderRequest(
#     symbol = 'ADBE',
#     notional = 250,
#     side = OrderSide.BUY,
#     type = 'market',
#     time_in_force = TimeInForce.DAY
# )

# market_order = trading_client.submit_order(market_order_data)