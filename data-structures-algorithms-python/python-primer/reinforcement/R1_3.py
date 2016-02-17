def minmax(data):
    '''
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    >>> minmax([1,3,5,3,2,1,0,-1,2,6,3])
    (-1, 6)
    >>> minmax([1,393,45,303,574,5,5,9])
    (1, 574)
    >>> minmax([10,True, 500, 28, False, 12])
    (False, 500)
    '''
    data = sorted(data)
    smallest = data[0]
    largest = data[0]
    for n in data:
        smallest = n if n < smallest else smallest
        largest = n if n > largest else largest
    return (smallest, largest)
