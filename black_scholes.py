from scipy.stats import norm
from math import exp, log, sqrt


# This module contains the function to calculate the Black-Scholes option pricing formula.


def price(st, k, r, t, sigma, option_type):
    """ This function calculates the price of an option using the Black-Scholes formula
    :param st: price of the underlying asset
    :param k: strike price
    :param r: risk-free interest rate
    :param t: time to maturity in years
    :param sigma: volatility of the underlying asset
    :param option_type: type of the option (call or put)
    :return: price of the option
    """
    norm_dist = norm(0, 1)
    d1 = (1 / (sigma * sqrt(t))) * (log(st / k) + (r + (sigma ** 2) / 2) * t)
    d2 = d1 - sigma * sqrt(t)

    if option_type == 'call':
        return st * norm_dist.cdf(d1) - k * exp(- r * t) * norm_dist.cdf(d2)

    elif option_type == 'put':
        return - st * norm_dist.cdf(- d1) + k * exp(- r * t) * norm_dist.cdf(- d2)
