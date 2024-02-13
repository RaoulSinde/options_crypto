import black_scholes_pricing as bsp


class Option:
    def __init__(self, s0, k, r, t, sigma, option_type):
        self.s0 = s0
        self.k = k
        self.r = r
        self.t = t
        self.sigma = sigma
        self.option_type = option_type
        self.d1, self.d2 = self.calc_d1_d2()

    def calc_d1_d2(self):
        d1 = bsp.calc_d1(self.s0, self.k, self.r, self.t, self.sigma)
        d2 = bsp.calc_d2(d1, self.t, self.sigma)

        return d1, d2

    def call_price(self):

        return bsp.call_price(self.s0, self.k, self.r, self.t, self.d1, self.d2)

    def put_price(self):

        return bsp.put_price(self.s0, self.k, self.r, self.t, self.d1, self.d2)
