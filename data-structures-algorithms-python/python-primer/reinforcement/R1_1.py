def is_multiple(n, m):
    '''
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    >>> is_multiple(4, 2)
    True
    >>> is_multiple(0,10)
    True
    >>> is_multiple(22, 3)
    False
    '''
    return n == 0 or n % m == 0
