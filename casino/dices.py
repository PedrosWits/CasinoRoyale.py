import random
import math
from coins import BiasedCoin
from abc import ABCMeta, abstractmethod
from utils import areEqual, lcm, MAX_LIST_SIZE

class FairDie(object):

    def __init__(self, nsides):
        self.nsides = nsides

    def roll(self):
        return int(math.floor(r.random()*self.nsides))

class LoadedDie(object):
    __metaclass__ = ABCMeta

    def __init__(self, psides, verifyInput = True):
        if verifyInput:
            #psides should be different, we can verify that, but it
            if areEqual(psides):
                raise ValueError('The probabilities for the sides ' \
                                'are all equal making this a fair dice!')
            indixes = [i for i,pside in enumerate(psides) if pside < 0 or pside > 1]
            if len(indixes) > 0:
                ex = ValueError('You defined one or ' \
                        'more probabilities lower than 0 or greater than 1')
                ex.indexes = indixes
                raise ex
            soma = sum(psides)
            if soma != 1:
                ex = ValueError('The sum of the given probabilities is different than zero')
                ex.soma = soma
                raise ex
        # else, save the psides for later usage
        self.psides = psides
        # run pre_processing
        self.pre_process()

    @abstractmethod
    def pre_process(self):
        pass

    @abstractmethod
    def roll(self):
        pass


##################################################
#                                                #
####    START LOADED DICE IMPLEMENTATIONS    #####
#                                                #
##################################################

class LoadedDie(object):
    __metaclass__ = ABCMeta

    def __init__(self, psides, verifyInput = True):
        if verifyInput:
            #psides should be different, we can verify that, but it
            if areEqual(psides):
                raise ValueError('The probabilities for the sides ' \
                                'are all equal making this a fair dice!')
            indixes = [i for i,pside in enumerate(psides) if pside < 0 or pside > 1]
            if len(indixes) > 0:
                ex = ValueError('You defined one or ' \
                        'more probabilities lower than 0 or greater than 1')
                ex.indexes = indixes
                raise ex
            soma = sum(psides)
            if soma != 1:
                ex = ValueError('The sum of the given probabilities is different than zero')
                ex.soma = soma
                raise ex
        # else, save the psides for later usage
        self.psides = psides
        # run pre_processing
        self.pre_process()

    @abstractmethod
    def pre_process(self):
        pass

    @abstractmethod
    def roll(self):
        pass

class FairDie(object):

    def __init__(self, nsides):
        self.nsides = nsides

    def roll(self):
        return int(math.floor(r.random()*self.nsides))

#
#
#   Algorithms for implementing a loaded Die
#

#   Simulates a Loaded Die from a Fair Die
#
#   Beware: A Fair Die has been mutated into a loaded die!!
#           It only works with Fractions as input!!

class MutatedDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(MutatedDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pfracs = reduce(lambda x: Fraction(x), self.psides)
        denominators = [pfrac.denominator for pfrac in pfracs]
        self.L = lcm(denominators)
        if self.L > MAX_LIST_SIZE:
            ex = OverflowError('The resulting value for L (least common multiplier)' \
                    ' for the given list of fractions is bigger than allowed.' \
                    '. Please try again with a different list of psides.')
            ex.L = self.L
            ex.MAX_LIST_SIZE = MAX_LIST_SIZE
            raise ex
        self.A = []
        for i,pfrac in enumerate(pfracs):
            size = int(self.L*pfrac)
            for j in range(size):
                self.A.append(i)

    def roll(self):
        index = FairDie(self.L).roll()
        return self.A[index]

#   Simulates a Loaded Die from Biased Coins
#
#   Beware: A coined die is ahead!!
class CoinedDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(CoinedDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pass

    def roll(self):
        pass

#   Simulates a Loaded Die from a the roulette wheel selection method
#
#   Beware: High rotations ahead! You may get dizzy!!
class RouletteDie(LoadedDie):
    def __init__(self, psides, skipVerification = True):
        super(RouletteDie, self).__init__(psides, skipVerification)

    def pre_process(self):
        pass

    def roll(self):
        pass

    def optimize(self):
        pass

#   Simulates a Loaded Die from a combination of fair dies and biased coins
#
#   Beware: Appearances can be deceiving!!
class HybridDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(HybridDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pass

    def roll(self):
        pass

#   Simulates a Loaded Die using the Naive Alias Method
#
#   Beware: A prize for one ignorant clown is ahead!
class NaiveDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(NaiveDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pass

    def roll(self):
        pass

#   Simulates a Loaded Die using the Alias Method
#
#   Beware: Confidential information!!
class AliasDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(AliasDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pass

    def roll(self):
        pass

#   Simulates a Loaded Die from Biased Coins
#
#   Beware: The next step is into hell!!
class VosesDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(VosesDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pass

    def roll(self):
        pass


