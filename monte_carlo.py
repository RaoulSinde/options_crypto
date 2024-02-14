import random
import black_scholes as bs
import matplotlib.pyplot as plt
from math import sqrt

colors = ['r', 'g', 'b', 'y']


def monte_carlo_bs(s0, k, r, t, sigma, option_type, er, sims=200, horizon=180):
    """ This function calculates Monte Carlo simulations for the price of options
    :param s0: price of the underlying asset
    :param k: strike price
    :param r: risk-free interest rate
    :param t: time to maturity in years
    :param sigma: volatility of the underlying asset
    :param option_type: type of the option (call or put)
    :param er: yearly expected return for the underlying asset
    :param sims: number of simulations
    :param horizon: number of days of simulations (number of simulated prices)
    """
    er = er / 365
    vol = sigma / sqrt(365)

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlabel("Time")
    ax.set_ylabel("Call price")
    ax.set_title("Monte Carlo simulations")

    for sim in range(sims):
        asset_price = [s0]
        option_price = [bs.price(s0, k, r, t, sigma, option_type)]

        for day in range(1, horizon):

            asset_price.append(asset_price[-1] * (1 + random.gauss(er, vol)))
            option_price.append(bs.price(asset_price[-1], k, r, t-day/365, sigma, option_type))

        random_index = random.randint(0, len(colors) - 1)
        ax.plot(option_price, color=colors[random_index], linewidth=0.5)

    plt.ioff()
    plt.legend()
    plt.show()
