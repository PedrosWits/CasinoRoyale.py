import random
import math
from fractions import Fraction
from decimal import Decimal
from coins import BiasedCoin, Coin
from abc import ABCMeta, abstractmethod
from utils import areEqual, lcm, MAX_LIST_SIZE

class LoadedDie(object):
    __metaclass__ = ABCMeta

    def __init__(self, psides, verifyInput = True):
        if verifyInput:
            #psides should be different, we can verify that, but it
            if areEqual(psides):
                raise ValueError('The probabilities for the sides ' \
                                'are all equal making this a fair dice!')
            soma = sum(psides)
            if soma != 1:
                ex = ValueError('The sum of the given probabilities is different than one!')
                ex.soma = soma
                raise ex
            indixes = [i for i,pside in enumerate(psides) if pside <= 0 or pside > 1]
            if len(indixes) > 0:
                ex = ValueError('You defined one or ' \
                        'more probabilities lower than 0 or greater than 1')
                ex.indexes = indixes
                raise ex
        # else, save the psides for later usage
        self.psides = psides
        self.nsides = len(psides)
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
        return int(math.floor(random.random()*self.nsides))

##################################################
#                                                #
####    START LOADED DICE IMPLEMENTATIONS    #####
#                                                #
##################################################


#   Simulates a Loaded Die from a Fair Die
#
#   Beware: A Fair Die has been mutated into a loaded die!!
#           It only works with Fractions as input!!

class MutatedDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(MutatedDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pfracs = []
        for pside in self.psides:
            pfracs.append(Fraction(Decimal(str(pside))))
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
        mass = 1.0
        for i in range(self.nsides):
            pi = self.psides[i]
            if Coin(pi/mass).toss() == 1:
                return i
            else:
                mass -= pi

#   Simulates a Loaded Die from a the roulette wheel selection method
#
#   Beware: High rotations ahead! You may get dizzy!!
class RouletteDie(LoadedDie):
    def __init__(self, psides, skipVerification = True):
        super(RouletteDie, self).__init__(psides, skipVerification)

    def pre_process(self):
        A = []
        A.append(self.psides[0])
        for i in range(1, self.nsides):
            val = A[i-1] + self.psides[i]
            A.append(val)
        self.A = A
        #print A

    def roll(self):
        x = random.random()
        self.x = x
        #print ("x = %.2f") % x
        head = 0
        tail = len(self.A)-1
        candidate = -1

        # Binary search - returns index of smallest element in A larger than x
        while head <= tail:
            mid = (head + tail)/2
            #print "Head = %d, Mid = %d, Tail = %d" % (head, mid, tail)
            val = self.A[mid]
            if val > x:
                candidate = mid
                tail = mid-1
            elif val < x:
                head = mid+1
        #
        if self.A[mid] >= x:
            return mid
        else:
            return candidate

    def optimize(self):
        pass

#   Simulates a Loaded Die from a combination of fair dies and biased coins
#
#   Beware: Appearances can be deceiving!!
class HybridDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(HybridDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        pmax = max(self.psides)
        self.coins = []
        for i in range(self.nsides):
            self.coins.append(self.psides[i]/pmax)

    def roll(self):
        while True:
            index = FairDie(self.nsides).roll()
            if Coin(self.coins[index]).toss() == 1:
                return index

#   Simulates a Loaded Die using the Naive Alias Method
#
#   Beware: A prize for one ignorant clown is ahead!
class NaiveDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(NaiveDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        raise NotImplementedError("I haven't yet implemented this data structure."\
                "I'm sorry. Please try a different one")
        new_probs[:] = [i * self.nsides for i in self.psides]
        print "New probabilities: "
        print new_probs
        self.Alias = [0] * self.nsides
        self.Prob = [0] * self.nsides
        for j in range(1, self.nsides):
            (index_l, pl) = findLower(new_probs, 1)
            print "l = %d, Pl = %.2f" % (index_l, pl)
            (index_g, pg) = findGreater(new_probs, 1, index_l)
            print "g = %d, Pg = %.2f" % (index_g, pg)
            self.Prob[index_l] = pl
            self.Alias[index_l] = index_g
            print self.Prob
            print self.Alias
            del new_probs[index_l]
            new_probs[index_g] = pg - (1 - pl)
            print new_probs
        # Let i be the last probability remaining, which must have weight 1
        # Set Prob[i] = 1


    def roll(self):
        pass

#   Simulates a Loaded Die using the Alias Method
#
#   Beware: Confidential information!!
class AliasDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(AliasDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        raise NotImplementedError("I haven't yet implemented this data structure."\
                "I'm sorry. Please try a different one")
        self.Alias = [0] * self.nsides
        self.Prob = [0] * self.nsides


    def roll(self):
        pass

#   Simulates a Loaded Die from Biased Coins
#
#   Beware: The next step is into hell!!
class VosesDie(LoadedDie):
    def __init__(self, psides, verifyInput = True):
        super(VosesDie, self).__init__(psides, verifyInput)

    def pre_process(self):
        self.Alias = [0] * self.nsides
        self.Prob = [0] * self.nsides
        Small = []
        Large = []
        new_probs = [i * self.nsides for i in self.psides]
        for i,prob in enumerate(new_probs):
            if prob < 1:
                Small.append(i)
            else:   #prob >= 1
                Large.append(i)
        while Small and Large:
            l = Small.pop(0)
            g = Large.pop(0)
            self.Prob[l] = new_probs[l]
            self.Alias[l] = g
            new_probs[g] = (new_probs[g] + new_probs[l]) - 1
            if new_probs[g] < 1:
                Small.append(g)
            else:
                Large.append(g)
        while Large:
            g = Large.pop(0)
            self.Prob[g] = 1
        while Small:
            l = Small.pop(0)
            self.Prob[l] = 1
        #print self.Prob
        #print self.Alias

    def roll(self):
        i = FairDie(self.nsides).roll()
        if BiasedCoin(self.Prob[i]).toss() == 1:
            return i
        else:
            return self.Alias[i]


################################################################
#
#   COMMON FUNCTIONS FOR THE ALIAS METHODS
#
################################################################


def findLower(probs, threshold):
    for i,prob in enumerate(probs):
        if prob <= threshold:
            return (i, prob)

def findGreater(probs, threshold, skipIndex = -1):
    for i, prob in enumerate(probs):
        if i == skipIndex:
            continue
        if prob >= threshold:
            return (i, prob)

