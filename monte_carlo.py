import random
# import black_scholes as bs
import matplotlib.pyplot as plt
from math import sqrt

mc_sims = 200
T = 180

c0 = 100
er = 0.1 / 365
vol = 0.15 / sqrt(365)
k = 110
r = 0.02
t = 1 / 2
sigma = 0.15

colors = ['r', 'g', 'b', 'y']


def monte_carlo_bs():
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlabel("Time")
    ax.set_ylabel("Asset price")
    ax.set_title("Monte Carlo simulation")

    for sim in range(mc_sims):
        asset_price = [c0]

        for day in range(1, T):
            # call_price = bs.price(asset_price[-1], k, r, t-day/365, sigma, 'call')

            asset_price.append(asset_price[-1] * (1 + random.gauss(er, vol)))

        random_index = random.randint(0, len(colors) - 1)
        ax.plot(asset_price, color=colors[random_index], linewidth=0.5)

    plt.ioff()
    plt.legend()
    plt.show()


monte_carlo_bs()
