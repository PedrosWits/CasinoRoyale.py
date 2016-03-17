# http://stackoverflow.com/questions/855191/how-big-can-a-python-array-get
MAX_LIST_SIZE = 536870912

# Help global functions

def areEqual(lst):
    return not lst or lst.count(lst[0]) == len(lst)

# Greatest Common Divisor of two numbers using
# Euclid's algorithms
def gcd(a,b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)

# Calculate the Least Common Multiplier on a list of numbers
def lcm(numbers):
    return reduce(lambda x,y: x*y/gcd(x,y), numbers)
