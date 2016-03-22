# CasinoRoyale.py

##### A small python library for tossing coins and rolling dices!

![Just a random casino for y'all!](/../just-for-image/casino.jpg?raw=true "Sauron's Casino")

---

## Motivation:

This is a small python module that was motived by a very interesting piece written by Keith Schwarz, entitled:

  [*Darts, Dice, and Coins: Sampling from a Discrete Distribution*](http://www.keithschwarz.com/darts-dice-coins)

In this article, he analyses different data structures and algorithms for representing and rolling a loaded die.
I find his presentation of the problem and various solutions to be an example of how to approach computational problems.
This is exacly the kind of step-by-step problem-solving and analysis skills we want to foster in early coders.

So, I decided to implement the data structures and algorithms in a python module which may be easily used on a different project, or even provide a good teaching tool someday.

---

## Coins:

+ Create a fair coin, with equal tossing chances:
```python
  from casino.coins import FairCoin
  
  fair_coin = FairCoin()
```

+ Create a biased coin:
```python
  from casino.coins import BiasedCoin
  
  biased_coin = BiasedCoin(0.7)
  # or with
  biased_coin = BiasedCoin(pheads=0.7)
```

+ Or just create an arbitrary coin:
```python
  from casino.coins import Coin
  
  coin = Coin(0.1337)
  # or with
  coin = Coin(pheads=0.1337)
```

+ Toss any coin with:
```python
  result = coin.toss()
```
result is evaluated to **1** if **heads** or **0** if **tails**

**Constructors raise _Value Error_ when:**
+ Probability of heads is lower than zero **or** greater than 1.
+ You try to create a **Biased** Coin as a **Fair** Coin (i.e. with pheads = 0.5)

---

## Dices:

+ Create a fair die with *n* sides, with equal rolling chances for all sides:
```python
  from casino.dices import FairDie
  
  fair_die = FairDie(6)
  # or
  fair_die = FairDie(nsides=6)
```

+ Roll any die with:
```python
  face = die.roll()
```
face is an integer value **between 0 and n-1**

#### Creating loaded dices:

Creating a loaded die requires a list containing the probability of rolling each face of the die.  
The length of the list corresponds to the number of faces of the die.

However, **LoadedDie** is an abstract class used as a common base for different possible implementations.  
We provide 7 different implementations of the **Loaded Die** (5 currently), based on Keith's post:

| Implementation | Simulates a loaded die using | Implemented (y/n) |
| -------------  |:-------------:|:-----------------------------:|
| *MutatedDie* | A fair die | y |
| *CoinedDie*  | Biased coins | y |
| *RouletteDie* | The roulette wheel selection method | y|
| *HybridDie*   | A combination of fair dices and biased coins | y |
| *NaiveDie* | The Naive Alias method  | n |
| *AliasDie*  | The Alias method | n |
| *VosesDie* | The Voses Alias method | y |

The constructor parameters and methods for all classes are the same.  
For instance, you can create Mutated Dies like this:

```python
  from casino.dices import MutantDie
  
  mutant = MutatedDie([0.3, 0.2, 0.5])
  # or
  mutant2 = MutatedDie(psides = [0.7, 0.2, 0.1])
  # or 
  mutant3 = MutatedDie(psides = [0.5, 0.1, 0.1, 0.3], verifyInput = True)
  # or
  # this does not raise a ValueError exception
  mutant4 = MutatedDie(psides = [0.4, 0.5, 0.2], verifyInput = False)
  # or
  # this raises a ValueError exception
  mutant5 = MutatedDie([0.4, 0.5, 0.2], True)
```
Or use other implementations of LoadedDie in the same manner:

```python
  from casino.dices import CoinedDie, RouletteDie, HybridDie, VosesDie
  
  psides = [0.2, 0.3, 0.5]
  
  die1 = CoinedDie(psides)
  die2 = RouletteDie(psides)
  die3 = HybridDie(psides)
  die4 = VosesDie(psides)
```

You can review the differences between the several implementations in the table below, extracted from
Keith's post (I hope that's okay with him):

![A valuable comparison.](/../just-for-image/loaded_implementations.png?raw=true "Rock n' rollin")

#### Implementing your own loaded die:

You can implement your own loaded die by extending the **LoadedDie** class
and implementing the two base abstract methods: *pre_process(self)* and *roll(self)*:

```python
  MyBadassDie(LoadedDie):
      def __init__(self, psides, verifyInput = True):
          super(MyBadassDie, self).__init__(psides, verifyInput)
    
      def pre_process(self):
          ...
    
      def roll(self):
          ...
```

**Note**: You don't need to call *pre_process()* because the parent class **LoadedDie**
already does that work for you.

---

#### Additional Considerations:

+ The second parameter in the LoadedDice constructor takes a **boolean** which if *True* checks if the passed list
of probabilities respects the following (obvious) properties:
 * The sum of probabilities must equal 1 and only 1.
 * There can be no probability greater than one or lower/equal to zero.
 * All probabilites can not hold the same value (1/nfaces) - that would make it a fair die.

+ On the implementation of a Loaded Die using a Fair Die, we capped the *psides* list size based
on an answer provided at [stackoverflow](http://stackoverflow.com/questions/855191/how-big-can-a-python-array-get).
Nevertheless, as stated by Keith, the usable memory required to hold in memory the size of the *L* array can easily
be larger than the available memory in RAM. Thus, checking the size of the array against the value of MAX_LIST_SIZE, when you can trigger an overflow error with just a two value list (see Keith's example) does look in fact like a useless, pointless operation. Nevertheless it's there and if you don't like it you can just simply take it off.

+ I am using nose for unit-testing, but you can run them at (/casino/tests) using your favourite python testing framework or library.

---

## The End

Any comments or suggestions, email me to ppintodasilva@gmail.com  

Pedro Pinto da Silva,  
Porto, Portugal - March, 2016
