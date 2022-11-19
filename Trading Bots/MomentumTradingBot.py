from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import yfinance as yf
import datetime as dt
import pandas as pd
from pandas.tseries.offsets import MonthBegin, MonthEnd 

bigTech = ['meta', 'aapl', 'amzn', 'goog', 'pypl', 'adbe', 'nvda', 'tsla']

today = dt.date.today()

startDate = today - MonthBegin(1)
endDate = today - MonthEnd(1)

df = yf.download(bigTech, start=startDate, end=endDate)
prices = df['Adj Close']
dailyReturns = prices.pct_change().dropna()
dailyCumulativeReturns = (1+dailyReturns).cumprod()+1
dailyCumulativeReturns.index = pd.to_datetime(dailyCumulativeReturns.index)
results = dailyCumulativeReturns[dailyCumulativeReturns.index == max(dailyCumulativeReturns.index)]
winners = results.apply(lambda x: x.nlargest(2).index.tolist(), axis=1)[0][0:2]
lmtPrices = prices[prices.index == max(prices.index)][[winners[0],winners[1]]]

API_KEY = 'PKWF88ZVMO01Z9RM8FL8'
SECRET_KEY = 'Ff9vN4vkdkRS6vi9koeWLThFryFKpq1rr0iMQgye'

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

market_order_data1 = MarketOrderRequest(
    symbol = winners[0],
    notional = 250,
    side = OrderSide.BUY,
    type = 'market',
    time_in_force = TimeInForce.DAY
)

market_order_data2 = MarketOrderRequest(
    symbol = winners[1],
    notional = 250,
    side = OrderSide.BUY,
    type = 'market',
    time_in_force = TimeInForce.DAY
)

market_order1 = trading_client.submit_order(market_order_data1)
market_order2 = trading_client.submit_order(market_order_data2)



