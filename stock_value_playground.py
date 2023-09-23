import yfinance as yf

ticker = ['MSFT', 'AAPL', 'CSCO']

for items in ticker:
    stocks = yf.Ticker(items)

    current_price = stocks.info['currentPrice']

    print('Current price of ' + items + ' is '+ str(current_price) + '$')