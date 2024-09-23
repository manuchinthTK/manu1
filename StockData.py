import yfinance as yf

ticker = input("Enter the ticker :")
from_date = input("Enter the start date (yyyy-mm-dd) :")
to_date = input("Enter the end date (yyy-mm-dd) :")

stock_data = yf.download(ticker , start = from_date , end = to_date)
stock_data.to_html("stock_data.html")
print("Stock data written to stock_data.csv")