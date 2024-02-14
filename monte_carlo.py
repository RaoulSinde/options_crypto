import random
# import black_scholes as bs
import matplotlib.pyplot as plt
from math import sqrt

colors = ['r', 'g', 'b', 'y']


def monte_carlo_bs(s0, er, vol, sims=200, horizon=180):

    er = er / 365
    vol = vol / sqrt(365)

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlabel("Time")
    ax.set_ylabel("Asset price")
    ax.set_title("Monte Carlo simulations")

    for sim in range(sims):
        asset_price = [s0]

        for day in range(1, horizon):
            # call_price = bs.price(asset_price[-1], k, r, t-day/365, sigma, 'call')

            asset_price.append(asset_price[-1] * (1 + random.gauss(er, vol)))

        random_index = random.randint(0, len(colors) - 1)
        ax.plot(asset_price, color=colors[random_index], linewidth=0.5)

    plt.ioff()
    plt.legend()
    plt.show()
