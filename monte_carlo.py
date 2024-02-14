import random
import black_scholes as bs
import matplotlib.pyplot as plt
from math import sqrt

mc_sims = 50
T = 100

c0 = 100
er = 0.1 / 365
vol = 0.15 / sqrt(365)
k = 110
r = 0.02
t = 1 / 2
sigma = 0.15


def monte_carlo_bs():
    plt.ion()  # Activer le mode interactif
    fig, ax = plt.subplots()
    ax.set_xlabel("Time Increments")
    ax.set_ylabel("Stock Price")
    ax.set_title("Geometric Brownian Motion")

    for sim in range(mc_sims):
        asset_price = [c0]

        for day in range(1, T):
            d1 = bs.calc_d1(asset_price[-1], k, r, t, sigma)
            d2 = bs.calc_d2(d1, t, sigma)
            call_price = bs.call_price(asset_price[-1], k, r, t-day/365, d1, d2)

            asset_price.append(asset_price[-1] * (1 + er + vol * random.gauss(0, 1)))

            ax.plot(asset_price, color='blue', linewidth=0.5)

    plt.ioff()  # Désactiver le mode interactif à la fin de la boucle
    plt.legend()
    plt.show()


monte_carlo_bs()
