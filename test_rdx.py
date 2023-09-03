from rdx import *
from string import hexdigits 



if __name__ == '__main__':
    #int_to_digits & digits_to_int
    #Check both directions
    for b in range(2, 100):
        for n in range(100):
            assert n == digits_to_int(int_to_digits(n, b), b)
    
    
    #Some hardcoded values
    assert int_to_digits(0, 2) == []
    assert int_to_digits(1, 2) == [1]
    assert int_to_digits(2, 2) == [0, 1]
    assert int_to_digits(3, 2) == [1, 1]
    assert int_to_digits(4, 2) == [0, 0, 1]
    assert int_to_digits(5, 2) == [1, 0, 1]
    
    #https://stackoverflow.com/a/28666223/7367030
    assert int_to_digits(67854**15-102, 577) == [455, 264, 197, 435, 0, 28,
            131, 517, 100, 483, 41, 25, 149, 538, 292, 82, 16, 23, 28, 486,
            524, 285, 431, 96, 131, 473, 4]
    
    
    #Built-in number system conversion functions
    for n in range(1, 1000):
        #Binary, https://docs.python.org/3/library/functions.html#bin
        d = list(map(int, reversed(format(n, 'b'))))
        assert d == int_to_digits(n, 2)
        assert n == digits_to_int(d, 2)
        
        #Octal, https://docs.python.org/3/library/functions.html#oct
        d = list(map(int, reversed(format(n, 'o'))))
        assert d == int_to_digits(n, 8)
        assert n == digits_to_int(d, 8)
        
        #Decimal
        d = list(map(int, reversed(format(n, 'd'))))
        assert d == int_to_digits(n, 10)
        assert n == digits_to_int(d, 10)
        
        #Hexadecimal, https://docs.python.org/3/library/functions.html#hex
        d = list(map(lambda c: int(c, 16), reversed(format(n, 'x'))))
        assert d == int_to_digits(n, 16)
        assert n == digits_to_int(d, 16)
        
        #int(x, base), https://docs.python.org/3/library/functions.html#int
        for b in range(2, 16+1):
            s = ''.join(hexdigits[d] for d in reversed(int_to_digits(n, b)))
            assert n == int(s, b)
    
    
    
    #len_int_to_digits
    #Compare to actual conversion
    for b in range(2, 100):
        for n in range(100):
            assert int_to_len_digits(n, b) == len(int_to_digits(n, b))
    
    
    #Some hardcoded values
    #https://stackoverflow.com/a/2189827/7367030
    assert int_to_len_digits(int(71*'9'), 10) == 71
    #https://stackoverflow.com/q/12385040/7367030
    assert int_to_len_digits(int('''
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450'''
        .replace('\n', '').replace(' ', '')), 10) == 1000
    
    
    
    #digits_to_characters & characters_to_digits
    for n in range(1, 1000):
        #Check both directions
        for b in range(2, 20):
            d = int_to_digits(n, b)
            assert characters_to_digits(digits_to_characters(d)) == d
        
        #Compare to hex
        d = int_to_digits(n, 16)
        s = format(n, 'x')
        assert list(reversed(s)) == digits_to_characters(d)
        assert characters_to_digits(list(reversed(s))) == d
    
    
    #digits_to_string & string_to_digits
    for b in range(2, 16+1):
        for n in range(1, 1000):
            #Check both directions
            d = int_to_digits(n, b)
            assert string_to_digits(digits_to_string(d)) == d
            #Compare to int(x, base)
            #https://docs.python.org/3/library/functions.html#int
            assert int(digits_to_string(d), b) == n
