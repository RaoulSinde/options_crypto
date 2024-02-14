import black_scholes as bs


class Option:
    """
    This class defines an Option that has different characteristics:
        st is the price of the underlying asset on the date t
        k is the strike price
        r is the risk-free interest rate
        t is the time to maturity in years
        sigma is the volatility of the underlying asset
        option_type is the type of the option (call or put)

    The class has also a method called price that returns the price of the option
    The formula is implemented in the black_scholes_pricing.py file that is called in the method price

    """

    def __init__(self, st, k, r, t, sigma, option_type):
        self.st = st
        self.k = k
        self.r = r
        self.t = t
        self.option_type = option_type
        self.sigma = sigma

    def price(self):
        return bs.price(self.st, self.k, self.r, self.t, self.sigma, self.option_type)
