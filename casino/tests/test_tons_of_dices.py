from nose.tools import eq_, ok_, raises, nottest
from casino.dices import FairDie, MutatedDie, CoinedDie, RouletteDie, HybridDie
import random

# Test all loaded implementations with the same inputs
SEED_LOADED = 1337
N_RUNS = 10
PSIDES_LOADED_1 = [0.4, 0.1, 0.2, 0.1, 0.05, 0.15]
EXPECTED_LOADED_1 = [2, 2, 0, 2, 0, 4, 0, 3, 5, 0]
EXPECTED_LOADED_2 = [2, 1, 5, 0, 2, 2, 5, 5, 3, 0]
EXPECTED_LOADED_3 = [0, 5, 5, 0, 2, 2, 1, 3, 3, 4]

def test_fair_is_fair():
    random.seed(1000)
    expected = [4,4,0,2,2,3,5,0,4,2,2]
    nsides = 6
    die = FairDie(nsides)
    result = []
    for i in range(len(expected)):
        result.append(die.roll())
    eq_(expected, result)

@raises(ValueError)
def test_bad_loaded():
    one_third = 1.0/3.0
    psides = [one_third, one_third, one_third]
    baddie = MutatedDie(psides)

@raises(ValueError)
def test_bad_loaded2():
    psides = [0.2, 0.5, 0.5]
    baddie2 = MutatedDie(psides)

@raises(ValueError)
def test_bad_loaded3():
    psides = [-1.0, 1.0, 1.0]
    baddie3 = MutatedDie(psides)

@raises(ValueError)
def test_bad_loaded4():
    psides = [-0.1, 0.8, 0.3]
    baddie4 = MutatedDie(psides)

def test_all_loaded_dices():
    eq_(die_rundown(MutatedDie(PSIDES_LOADED_1)), EXPECTED_LOADED_1)
    eq_(die_rundown(CoinedDie(PSIDES_LOADED_1)), EXPECTED_LOADED_2)
    eq_(die_rundown(RouletteDie(PSIDES_LOADED_1)), EXPECTED_LOADED_1)
    eq_(die_rundown(HybridDie(PSIDES_LOADED_1)), EXPECTED_LOADED_3)

@nottest
def die_rundown(die):
    random.seed(SEED_LOADED)
    result = []
    for i in range(N_RUNS):
        result.append(die.roll())
    return result
