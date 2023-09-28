import yfinance as yf

# Intrinsic value = Earnings per share (EPS) x (1 + r) x P/E ratio

# each ticker has to be seperated by ','
# stock_list  = ['AAPL', 'AIR.PA', 'AXP',	'BAC', 'CEZ.PR', 'CSCO', 'CVS', 'CZG.PR', 'DIS', 'GPRO', 'GRMN', 'INTC', 
#                'KBC.BR', 'KO' ,'MSFT', 'NKE', 'PG', 'RIO', 
#                'SHLS', 'SONY', 'TTWO', 'UL', 'VOW.DE']

stock_list = ['AAPL', 'AXP']

print(f"Stock count", len(stock_list))

# growth rate in %
growth_rate = 0.05

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

        try:
            eps = ticker.info['trailingPE']
            
            pe_list.append(eps)

        except KeyError:
            continue

    return pe_list

def current_price(stock):
    """Returns current price of a given stock"""

    current_price_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        price = ticker.info['currentPrice']

        current_price_list.append(price)

    return current_price_list

def currency_symbol(stock):
    """Returns currency of a given stock"""

    currency_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        currency = ticker.info['currency']

        currency_list.append(currency)

    return currency_list


with open("instrinc_value.csv", "w") as f:

    for eps, pe, price, tickers, currency in zip(earnings_share(stock_list), pe_ratio(stock_list), current_price(stock_list), stock_list, currency_symbol(stock_list)):

        pe_str = str(round(pe, 2))

        price_str = str(round(price, 2))

        instrinc_value = round(eps * (1 + growth_rate) * pe, 2)

        instrinc_str = str(instrinc_value)

        # file
        print(f"Instrinc value of {tickers} is {instrinc_str} {currency} price is {price} {currency} and PE is {pe_str}", file=f)   
        #terminal 
        print(f"Instrinc value of {tickers} is {instrinc_str} {currency} price is {price} {currency} and PE is {pe_str}") 


def market_cap(stock):

    cap_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        price = ticker.info['marketCap']

        cap_list.append(price)

    return cap_list

print(market_cap(stock_list))