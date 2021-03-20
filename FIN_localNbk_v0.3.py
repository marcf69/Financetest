#
# A executer seulement si les librairies ne sont pas installées.
#

pip install yfinance
pip install matplotlib
pip install seaborn


#################################################################


import yfinance as yf

msft = yf.Ticker("SPY")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="5d")


#####################
# Plot everything by leveraging the very powerful matplotlib package
#####################

import matplotlib.pyplot as plt
import seaborn


hist['Close'].plot(figsize=(16, 9))

#####################

data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
data_df.to_csv('aapl.csv')


#####################
# Download stock data then export as CSV
#####################
data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
data_df.to_csv('aapl.csv')