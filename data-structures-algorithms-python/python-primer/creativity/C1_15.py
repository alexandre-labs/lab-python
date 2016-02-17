def diff_numbers(seq):
    '''Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other
    (that is, they are distinct).
    >>> diff_numbers([1,2,3,4,5,6])
    True
    >>> diff_numbers([1,1,1,2,5,4,5,5,6,6,6,4,3,2,2])
    False
    '''
    return list(set(seq)) == seq
