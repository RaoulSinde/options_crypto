import random
import numpy as np
import black_scholes as bs
from math import sqrt

colors = ['r', 'g', 'b', 'y']


def monte_carlo_bs(s0, k, r, t, sigma, option_type, er, sims=100, horizon=100):
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
    :return: array of option prices for each simulation
    """
    er = er / 365
    vol = sigma / sqrt(365)

    asset_prices = np.zeros((sims, horizon))
    option_prices = np.zeros((sims, horizon))

    for sim in range(sims):
        asset_prices[sim, 0] = s0
        option_prices[sim, 0] = bs.price(s0, k, r, t, sigma, option_type)

        for day in range(1, horizon):
            asset_prices[sim, day] = asset_prices[sim, day - 1] * (1 + random.gauss(er, vol))
            option_prices[sim, day] = bs.price(asset_prices[sim, day], k, r, t - day / 365, sigma, option_type)

    return option_prices
