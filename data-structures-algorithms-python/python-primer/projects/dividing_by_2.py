def dividing_by_2(number):
    '''Write a Python program that can take a positive integer greater than 2
    as input and write out the number of times one must repeatedly divide this
    number by 2 before getting a value less than 2.
    >>> dividing_by_2(10)
    2
    '''
    if number <= 2:
        return 'Fail!'
    counter = 0
    while number >= 3:
        number /= 2
        counter += 1
    return counter
