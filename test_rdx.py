from rdx import *
from string import hexdigits 



if __name__ == '__main__':
    #Check both directions
    for b in range(2, 100):
        for n in range(100):
            assert n == from_digits(to_digits(n, b), b)
    
    
    #Some hardcoded values
    assert to_digits(0, 2) == []
    assert to_digits(1, 2) == [1]
    assert to_digits(2, 2) == [0, 1]
    assert to_digits(3, 2) == [1, 1]
    assert to_digits(4, 2) == [0, 0, 1]
    assert to_digits(5, 2) == [1, 0, 1]
    
    #https://stackoverflow.com/a/28666223/7367030
    assert to_digits(67854**15-102, 577) == [455, 264, 197, 435, 0, 28, 131,
            517, 100, 483, 41, 25, 149, 538, 292, 82, 16, 23, 28, 486, 524,
            285, 431, 96, 131, 473, 4]
    
    
    #Built-in number system conversion functions
    for n in range(1, 1000):
        #Binary, https://docs.python.org/3/library/functions.html#bin
        assert n == from_digits([int(c) for c in reversed(format(n, 'b'))], 2)
        assert format(n, 'b') == \
                ''.join(str(d) for d in reversed(to_digits(n, 2)))
        
        #Octal, https://docs.python.org/3/library/functions.html#oct
        assert n == from_digits([int(c) for c in reversed(format(n, 'o'))], 8)
        assert format(n, 'o') == \
                ''.join(str(d) for d in reversed(to_digits(n, 8)))
        
        #Hexadecimal, https://docs.python.org/3/library/functions.html#hex
        assert n == \
                from_digits([int(c, 16) for c in reversed(format(n, 'x'))], 16)
        assert format(n, 'x') == \
                ''.join(hexdigits[d] for d in reversed(to_digits(n, 16)))
        
        #int(x, base), https://docs.python.org/3/library/functions.html#int
        for b in range(2, 16+1):
            assert n == int(''.join(
                    hexdigits[d] for d in reversed(to_digits(n, b))), b)
