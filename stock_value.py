import yfinance as yf

# Intrinsic value = Earnings per share (EPS) x (1 + r) x P/E ratio

# each ticker has to be seperated by ','
stock_list  = ['AAPL', 'MSFT'] 

# growth rate in %
growth_rate = 0.1

def earnings_share(stock):
    """Gets EPS value for all tickers in a variable"""

    eps_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        eps = ticker.info['trailingEps']

        eps_list.append(eps)

    return eps_list
    
    

print(earnings_share(stock_list))