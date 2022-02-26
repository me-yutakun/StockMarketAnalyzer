# ticker=[x for x in input("Please insert space separated tickers:").split(" ")]
# start=input("Insert startdate (in yyyyMMdd format):")
# end=input("Insert enddate (in yyyyMMdd format):")
from StockMarketAnalyzer import *

def main():
    ticker = ['TCS.NS', 'MSFT']
    start = '20200101'
    end = '20200630'
    idf = source(ticker, start, end, 'yahoo')
    df = preprocessing(idf, ticker)
    nanhandler(df)

if __name__=="__main__":
    main()
