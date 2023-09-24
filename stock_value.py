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
    
    
def pe_ratio(stock):
    """Gets PE for all tickers in a variable"""

    pe_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        eps = ticker.info['trailingPE']

        pe_list.append(eps)

    return pe_list

for eps, pe, tickers in zip(earnings_share(stock_list), pe_ratio(stock_list), stock_list):

    instrinc = eps * (1 + growth_rate) * pe

    instrinc_str = str(instrinc)

    print(instrinc_str + tickers)


