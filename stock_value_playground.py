import yfinance as yf
import pprint 

ticker = ['MSFT', 'AAPL', 'CSCO']

# for items in ticker:
#     stocks = yf.Ticker(items)

#     current_price = stocks.info['currentPrice']

#     print('Current price of ' + items + ' is '+ str(current_price) + '$')

stocks = yf.Ticker('AXP')

# pprint.pprint(stocks.info)

cashflow = stocks.cashflow.loc['Free Cash Flow'].iloc[0]

print(cashflow)

