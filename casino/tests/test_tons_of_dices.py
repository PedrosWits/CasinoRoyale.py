from nose.tools import eq_, ok_, raises, nottest, assert_true
from casino.dices import FairDie, MutatedDie, CoinedDie, RouletteDie
from casino.dices import HybridDie, NaiveDie, AliasDie, VosesDie, LoadedDie
import random

# Test all loaded implementations with the same inputs

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

###
# Test algorithms asymptotic behavior - counts should approach psides as number
#   of iterations increases
###

PSIDES = ([0.20, 0.30, 0.40, 0.10],
          [0.10, 0.15, 0.25, 0.50],
          [0.10, 0.07, 0.03, 0.46, 0.04, 0.30],
          [0.89, 0.01, 0.01, 0.02, 0.07])
ERROR_INTERVAL = 0.020
SEPARATOR = "\n############################\n"
NITER = 10000
I_TITLE = "I = Input face probabilities"
O_TITLE = "O = Normalized probabilitie counters over %d iterations" % NITER
SOFT_SEPARATOR = "---"

@nottest
def count_faces(die, niter=NITER):
    face_counts = [0] * die.nsides
    for i in range(niter):
        face = die.roll()
        face_counts[face] += 1.0
    return [count/niter for count in face_counts]

@nottest
def assert_faces_counts(die, counts):
    if not hasattr(die, 'psides'):
        psides = [1.0/die.nsides] * len(counts)
    else:
        psides = die.psides
    for i,count in enumerate(counts):
        lower_bound = psides[i] - ERROR_INTERVAL
        upper_bound = psides[i] + ERROR_INTERVAL
        assert_true(lower_bound <= count <= upper_bound, \
                '\n\tFace %d: pside = %.2f \n\tResult: %.4f <= %.4f <= %.4f' %
                (i, psides[i], lower_bound, count, upper_bound))

def test_fair_die():
    random.seed()
    sides = 4
    die = FairDie(sides)
    assert_faces_counts(die, count_faces(die))

def test_loaded_die(DieClass):
    #if not isinstance(DieClass, LoadedDie):
    #    raise ValueError('Wrong parameter - must be a type of LoadedDie')
    random.seed()
    dices = []
    n = len(PSIDES)
    for i in range(n):
        dices.append(DieClass(PSIDES[i]))
    # evaluate each die
    counts = []
    for die in dices:
        this_count = count_faces(die)
        counts.append(this_count)
        assert_faces_counts(die, this_count)
    ## Print results
    print DieClass
    for i,count in enumerate(counts):
        print "I: %s" % "["+", ".join(["%.4f" % x for x in PSIDES[i]])+"]"
        print "O: %s" % str(count)
        print SOFT_SEPARATOR
    print SEPARATOR

def test_loaded_dices():
    print SEPARATOR
    print "Maximum error: %.3f\n" % ERROR_INTERVAL
    print I_TITLE
    print O_TITLE
    print SEPARATOR
    test_loaded_die(MutatedDie)
    test_loaded_die(CoinedDie)
    test_loaded_die(RouletteDie)
    test_loaded_die(HybridDie)
    test_loaded_die(VosesDie)
