from scipy.stats import norm
from math import exp, log, sqrt


def calc_d1(s0, k, r, t, sigma):
    return (1 / (sigma * sqrt(t))) * (log(s0 / k) + (r + (sigma ** 2) / 2) * t)


def calc_d2(d1, t, sigma):
    return d1 - sigma * sqrt(t)


def call_price(s0, k, r, t, d1, d2):
    return s0 * norm(d1) - k * exp(- r * t) * norm(d2)


def put_price(s0, k, r, t, d1, d2):
    return - s0 * norm(- d1) + k * exp(- r * t) * norm(- d2)
