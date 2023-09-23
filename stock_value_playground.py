import yfinance as yf

ticker = 'MSFT'
msft = yf.Ticker(ticker)

current_price = msft.info['currentPrice']

print('Current price of ' + ticker + ' is '+ str(current_price) + '$')
