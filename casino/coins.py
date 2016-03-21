import math
import random

EPS = 0.000001

class Coin(object):

    def __init__(self, pheads = 0.5):
        if pheads < 0 or pheads - 1 > EPS:
            raise ValueError('Probability of heads must be between [0,1]')
        self.pheads = pheads

    # Returns
    #   1 - heads
    #   0 - tails
    def toss(self):
        if random.random() < self.pheads:
            return 1
        else:
            return 0

class FairCoin(Coin):
    def __init__(self):
        super(FairCoin, self).__init__(pheads=0.5)

class BiasedCoin(Coin):
    def __init__(self, pheads):
        if pheads == 0.5:
            raise ValueError('A biased coin can not have the same  ' \
                                'probability for both sides (i.e. 1/2)')
        super(BiasedCoin, self).__init__(pheads)

