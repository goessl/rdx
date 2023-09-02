from functools import reduce
from sympy import log



def to_digits(n, b=10):
    """Returns the digits of number n in base b."""
    assert isinstance(n, int) and n>=0
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/28666223/7367030
    digits = []
    while n:
        digits += [n % b]
        n //= b
    return digits


def from_digits(d, b=10):
    """Returns the number represented by the digits d in base b."""
    assert all(isinstance(i, int) and i>=0 for i in d)
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/21782279/7367030
    return reduce(lambda n, y: b*n+y, reversed(d), 0)


def len_digits(n, b=10):
    assert isinstance(n, int) and n>=0
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/2189827
    #Sympy because of rounding errors see comments of
    #https://stackoverflow.com/a/28883802/7367030
    return int(log(n, b))+1 if n else 0
