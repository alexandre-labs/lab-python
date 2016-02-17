def is_even(k):
    '''
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    '''
    # >>> set(bin(x)[-1] for x in range(10000000) if x % 2 != 0)
    # {'1'}
    return bin(k)[-1] == 1
