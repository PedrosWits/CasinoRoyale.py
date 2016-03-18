from nose.tools import *
from casino.coins import Coin, FairCoin, BiasedCoin

def fair_coin():
    coin = FairCoin()
    assert coin.toss() == (0 or 1)

@raises(ValueError)
def bad_coin_low():
    coin = Coin(-1.5)

@raises(ValueError)
def bad_coin_high():
    coin = Coin(1.5)

def test():
    pass
