import yfinance as yf
import csv

# Intrinsic value = Earnings per share (EPS) x (1 + r) x P/E ratio

# each ticker has to be seperated by ','
# stock_list  = ['AAPL', 'AIR.PA', 'AXP', 'BAC', 'CEZ.PR', 'CSCO', 'CVS', 'CZG.PR', 'DIS', 'GPRO', 'GRMN', 'INTC', 
#                'KBC.BR', 'KO' ,'MSFT', 'NKE', 'PG', 'RIO', 
#                'SHLS', 'SONY', 'TTWO', 'UL', 'VOW.DE']

stock_list = ['MSFT', 'AAPL']

print(f"Stock count", len(stock_list), '\n')

# growth rate in %
growth_rate = 0.05

def earnings_share(stock):
    """Gets EPS value for all tickers in a variable"""

    #list of earnings per share
    eps_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        #get earning per share
        eps = ticker.info['trailingEps']

        #append list
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

        except:
            pe_list.append(-0)

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


def market_cap(stock):
    """Returns market cap of a given stock"""

    cap_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        cap = ticker.info['marketCap']

        cap_list.append(cap)

    return cap_list

def free_cf(stock):
    """Returns free cash flow of a given stock"""

    cashflow_list = []

    for items in stock:
        ticker = yf.Ticker(items)

        # get current free cash flow 'name' and location - iloc 0 = newest
        cashflow = ticker.cashflow.loc['Free Cash Flow'].iloc[0]

        cashflow_list.append(cashflow)

    return cashflow_list

# assign header columns 
headers = ['Ticker', 'Instrinc value', 'Current price', 'PE ratio', 'Free cashflow ratio', 'Currency'] 

writer = csv.DictWriter(open('test.csv', 'w'), delimiter=',', fieldnames=headers)

# Write the header names to the CSV file.
writer.writeheader()

for eps, pe, price, tickers, currency, cap, cf in zip(earnings_share(stock_list), 
                                                        pe_ratio(stock_list), 
                                                        current_price(stock_list), 
                                                        stock_list, 
                                                        currency_symbol(stock_list), 
                                                        market_cap(stock_list), 
                                                        free_cf(stock_list)):

    pe_str = str(round(pe, 2))

    price_str = str(round(price, 2))

    instrinc_value = round(eps * (1 + growth_rate) * pe, 2)

    instrinc_str = str(instrinc_value)

    ratio = int(cap / cf)

    ratio_str = str(ratio)

    #terminal 
    print(f"Instrinc value of {tickers}, is {instrinc_str} {currency} current price is {price_str} {currency} PE ratio is {pe_str} and free cashflow ratio is {ratio_str}") 

    row_data = {
        'Ticker': tickers,
        'Instrinc value': instrinc_str,
        'Current price': price_str,
        'PE ratio': pe_str,
        'Free cashflow ratio': ratio_str,
        'Currency': currency,
    }

    # Write the dictionary to the CSV file using the writerows() method of the DictWriter object.
    writer.writerow(row_data)

# Open the CSV file in read mode.
with open('test.csv', 'r') as input_csv_file:
    reader = csv.reader(input_csv_file)

    # Create a new CSV file in write mode.
    with open('test_without_empty_rows.csv', 'w', newline='') as output_csv_file:
        writer = csv.writer(output_csv_file)

        # Iterate over the rows in the input CSV file.
        for row in reader:
            # If the row is not empty, write it to the output CSV file.
            if row:
                writer.writerow(row)