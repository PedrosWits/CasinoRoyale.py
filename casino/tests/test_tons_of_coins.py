from nose.tools import raises
from casino.coins import Coin, FairCoin, BiasedCoin
import random

def test_toss_result():
    random.seed(1000)
    coin = FairCoin()
    assert coin.toss() == 0
    coin2 = Coin(0.3)
    assert coin2.toss() == 0
    coin3 = BiasedCoin(0.7)
    assert coin3.toss() == 1

@raises(ValueError)
def test_bad_coin_low():
    coin = Coin(-1.5)

@raises(ValueError)
def test_bad_coin_high():
    coin = Coin(1.5)

@raises(ValueError)
def test_fake_biased_coin():
    coin = BiasedCoin(0.5)

def test_biased_coin_1():
    coin = BiasedCoin(1.00000)
    coin.toss()

def test_biased_coin_0():
    coin = BiasedCoin(0)
    coin.toss()
