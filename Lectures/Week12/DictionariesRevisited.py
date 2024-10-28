# Dictionaries Revisited

dictionary = {"name":"John", "age":30, "city":"New York","cars": {"car1":"Ford","car2":"BMW", "car3":"Fiat"}}

print(dictionary['age'])
print(dictionary['cars'])

for car in dictionary['cars'].values():
    print("Cars:", car)








# Let's look at stocks!
portfolio = {'Stocks':[{'symbol':'GME','fullTimeEmployees': 12000,'currentPrice': 165, 'fiftyTwoWeekLow': 77.58, 'fiftyTwoWeekHigh': 344.66},
{'symbol':'AMC','fullTimeEmployees': 3046,'currentPrice': 23.3, 'fiftyTwoWeekLow': 8.31, 'fiftyTwoWeekHigh': 72.62},
{'symbol':'AMD','fullTimeEmployees': 15500,'currentPrice': 108.19, 'fiftyTwoWeekLow': 72.5, 'fiftyTwoWeekHigh': 164.46}]}

print(portfolio)
print(portfolio['Stocks'])
print(len(portfolio['Stocks']))


for stock in portfolio['Stocks']:

    print("---------------")
    print("Stock Symbol:",stock['symbol'])
    print("Number of Employees:", stock['fullTimeEmployees'])
    print("Current Price", stock['currentPrice'])







# Data returned back by yfinance
# if you want to play with this dataset you must install yFinance --> pip install yFinance
import yfinance as yf 
stock = yf.Ticker('AMD')

# Store stock info as dictionary
stock_dict = stock.info
print(stock_dict)
print(type(stock_dict))

print(stock_dict['symbol'],stock_dict['fullTimeEmployees'],stock_dict['currentPrice'],stock_dict['fiftyTwoWeekLow'],stock_dict['fiftyTwoWeekHigh'])

