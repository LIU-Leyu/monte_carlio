import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pandas_datareader import data as web
import yfinance as yf
# https://www.youtube.com/watch?v=6-dhdMDiYWQ

# import data
def get_stock(stocks, start, end):
    yf.pdr_override()
    data = web.get_data_yahoo(stocks, start, end)
    data = data[['Close']]
    # print(data.tail())
    # print(type(data))
    returns = data.pct_change()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    # print(mean_returns)
    # print(cov_matrix)
    return mean_returns, cov_matrix


stock_list = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stocks = [stock + '.AX' for stock in stock_list]  # appending the '.AX' suffix to each stock symbol in the stock_list
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=300)
mean_returns, cov_matrix = get_stock(stocks, start_date, end_date)

# numpy random.random function is used to generate an array of random values with the same length as mean_returns
weights = np.random.random(len(mean_returns))
# weights array is divided element-wise by the sum of all its elements using np.sum(weights) to normalize the values
# This ensures that the weights sum up to 1, representing proportions or percentages.
weights /= np.sum(weights)

# Monte Carlo Method
# num of simulation
mc_sims = 100
T = 100  # Timeframe in days

mean_matrix = np.full(shape=(T, len(weights)), fill_value=mean_returns)
mean_matrix = mean_matrix.T  # mean_matrix is transposed using the .T attribute to switch the rows and columns

# Array that we will store results in
portfolio_sims = np.fill(shape=(T, mc_sims), fill_value=0.0)

for n in range(mc_sims):
    # MC loops
    returns = mean_returns
    for i in range(T):
        daily_return = np.random.normal(returns, )  # Example daily return



