from scipy.stats import norm
from math import exp, log, sqrt


# This module contains the function to calculate the Black-Scholes option pricing formula.


def price(s, k, r, t, sigma, option_type):

    norm_dist = norm(0, 1)
    d1 = (1 / (sigma * sqrt(t))) * (log(s / k) + (r + (sigma ** 2) / 2) * t)
    d2 = d1 - sigma * sqrt(t)

    if option_type == 'call':
        return s * norm_dist.cdf(d1) - k * exp(- r * t) * norm_dist.cdf(d2)

    elif option_type == 'put':
        return - s * norm_dist.cdf(- d1) + k * exp(- r * t) * norm_dist.cdf(- d2)
