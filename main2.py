import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
# https://www.youtube.com/watch?v=LWc-9v8RVwM&t=306s

# load data
data = yf.download("TSLA")
data = data['Adj Close']

returns = np.log(1+data.pct_change())
mu, sigma = returns.mean(), returns.std()

# simulate returns for the next 252 days
sim_returns = np.random.normal(mu, sigma, 252)

initial_price = data.iloc[-1]

# simulated prices for the next 252 days
# (sim_returns + 1).cumprod(): calculates the cumulative product of (sim_returns + 1).
# The .cumprod() function computes the cumulative product along the specified axis,
# resulting in an array of cumulative returns over time.
# initial_price * (sim_returns + 1).cumprod(): The cumulative returns array is then multiplied by the initial price
# to compute the cumulative portfolio value over time.
sim_prices = initial_price * (sim_returns + 1).cumprod()

#
plt.plot(sim_prices)

num_sim = 100
num_days = 252
fig, ax = plt.subplots()

for i in range(num_sim):
    sim_returns = np.random.normal(mu, sigma, num_days)
    sim_prices = initial_price * (sim_returns + 1).cumprod()
    ax.plot(sim_prices)

# Add a horizontal line for the initial price
ax.axhline(initial_price, c='k')
plt.show()





