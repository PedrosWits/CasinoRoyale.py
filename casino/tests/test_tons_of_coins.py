from nose.tools import *
from casino.coins import Coin, FairCoin, BiasedCoin

def test_toss_result():
    coin = FairCoin()
    assert coin.toss() == (0 or 1)
    coin2 = Coin(0.3)
    assert coin2.toss() == (0 or 1)
    coin3 = BiasedCoin(0.7)
    assert coin3.toss() == (0 or 1)

@raises(ValueError)
def test_bad_coin_low():
    coin = Coin(-1.5)

@raises(ValueError)
def test_bad_coin_high():
    coin = Coin(1.5)
