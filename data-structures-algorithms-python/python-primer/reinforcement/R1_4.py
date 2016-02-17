import operator


def get_square(n):
    return n ** 2 if n >= 0 else 0


def sum_of_the_squares(n):
    '''
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.
    >>> sum_of_the_squares(5)
    30
    '''
    result = 0
    for smaller_number in range(n):
        result += get_square(smaller_number)

    return result
