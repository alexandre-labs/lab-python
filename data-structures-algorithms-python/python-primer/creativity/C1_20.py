from random import randint


def my_own_shuffle(seq):
    '''Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possi-
    ble order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    '''
    x = len(seq)
    while x > 0:
        pos_a = randint(0, x)
        pos_b = randint(0, x)

        seq[pos_a], seq[pos_b] = seq[pos_b], seq[pos_a]
        x -= 2
    return seq

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_own_shuffle(foo))
