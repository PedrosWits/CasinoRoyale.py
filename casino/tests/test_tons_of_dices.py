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

def test_binary_search():
    psides = [0.15, 0.15, 0.30, 0.20, 0.05, 0.10, 0.05]
    expected_A = [0.15, 0.30, 0.60, 0.80, 0.85, 0.95, 1.0]

    die = RouletteDie(psides)
    dif_A = [i - j for i, j in zip(expected_A, die.A)]
    for item in dif_A:
        assert abs(item) < 0.0001

    for number in range(1000):
        face = die.roll()
        x = die.x
        #print "x = %.2f, face = %d" % (x,face)
        if x <= 0.15:
            assert face == 0
        elif x > 0.15 and x <= 0.30:
            assert face == 1
        elif x > 0.30 and x <= 0.60:
            assert face == 2
        elif x > 0.60 and x <= 0.80:
            assert face == 3
        elif x > 0.80 and x <= 0.85:
            assert face == 4
        elif x > 0.85 and x <= 0.95:
            assert face == 5
        elif x > 0.95 and x <= 1.0:
            assert face == 6

@nottest
def die_rundown(die):
    random.seed(SEED_LOADED)
    result = []
    for i in range(N_RUNS):
        result.append(die.roll())
    return result
