from math import sqrt


def norm(v, p=None):
    '''
    The p-norm of a vector v = (v 1 , v 2 , . . . , v n )
    in n-dimensional space is de-fined as
    ||v|| = sqrt(v1^p + v2^p + v3^p + vn^p).
    For the special case of p = 2, this results in the traditional Euclidean
    norm, which represents the length of the vector. For example, the Eu-
    clidean norm of a two-dimensional
    with coordinates (4, 3) has a Euclidean norm of
    srqt(4**2 + 3**2) = sqrt(16 + 9) = sqrt(25) = 5.
    Give an implementation of a function named norm such that norm(v, p)
    returns the p-norm value of v and norm(v) returns
    the Euclidean norm of v. You may assume that v is a list of numbers.
    '''

    return sqrt((sum([x**(p or len(v)) for x in v])))
