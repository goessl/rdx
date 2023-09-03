from functools import reduce
from sympy import log
from string import digits, ascii_letters



def int_to_digits(n, b=10):
    """Returns the digits of number n in base b."""
    assert isinstance(n, int) and n>=0
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/28666223/7367030
    digits = []
    while n:
        digits += [n % b]
        n //= b
    return digits


def digits_to_int(d, b=10):
    """Returns the number represented by the digits d in base b."""
    assert all(isinstance(i, int) and i>=0 for i in d)
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/21782279/7367030
    return reduce(lambda n, y: b*n+y, reversed(d), 0)


def int_to_len_digits(n, b=10):
    """Returns the amount of digits
    the number n represented in base b needs."""
    assert isinstance(n, int) and n>=0
    assert isinstance(b, int) and b>=2
    
    #https://stackoverflow.com/a/2189827
    #Sympy because of rounding errors, see comments of
    #https://stackoverflow.com/a/28883802/7367030
    return int(log(n, b))+1 if n else 0



def digits_to_characters(d, alphabet=digits+ascii_letters):
    """Converts integer digits d to characters of the given alphabet."""
    assert all(isinstance(i, int) and 0<=i<len(alphabet) for i in d)
    return [alphabet[i] for i in d]

def characters_to_digits(s, alphabet=digits+ascii_letters):
    """Converts characters s of the given alphabet to integer digits."""
    assert all(isinstance(c, str) and len(c)==1 and c in alphabet for c in s)
    return [alphabet.index(c) for c in s]


def digits_to_string(d, alphabet=digits+ascii_letters):
    """Converts integer digits d
    to a right-to-left string in the given alphabet."""
    return ''.join(reversed(digits_to_characters(d, alphabet)))

def string_to_digits(s, alphabet=digits+ascii_letters):
    """Converts a right-to-left string s in the given alphabet
    to integer digits."""
    #wrap reversed(s), iterator -> iterable, so it won't get exhausted
    return characters_to_digits(list(reversed(s)), alphabet)
