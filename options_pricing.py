import black_scholes_pricing as bsp


class Option:
    """
    This class defines an Option that has different characteristics:
        s0 is the price of the underlying asset
        k is the strike price
        r is the risk-free interest rate
        t is the time to maturity in years
        sigma is the volatility of the underlying asset
        option_type is the type of the option (call or put)

    The class has also a method called price that returns the price of the option:
        to do so a method calculates d1 and d2 that are used in the Black-Scholes formula

    The formulas are implemented in the black_scholes_pricing.py file that is called in the method price
    and calc_d1_d2 of this class

    """
    def __init__(self, s0, k, r, t, sigma, option_type):
        self.s0 = s0
        self.k = k
        self.r = r
        self.t = t
        self.option_type = option_type
        self.sigma = sigma

        self.d1, self.d2 = self.calc_d1_d2()

    def calc_d1_d2(self):
        d1 = bsp.calc_d1(self.s0, self.k, self.r, self.t, self.sigma)
        d2 = bsp.calc_d2(d1, self.t, self.sigma)

        return d1, d2

    def price(self):

        if self.option_type == 'call':
            return bsp.call_price(self.s0, self.k, self.r, self.t, self.d1, self.d2)

        elif self.option_type == 'put':
            return bsp.put_price(self.s0, self.k, self.r, self.t, self.d1, self.d2)
