import itertools


def one_list(nested_list):
    """Dismount a nested list in one simples list

    >>> one_list([[1,2,3], [4,5,6], [7,8,9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    :nested_list: a list object with another lists as elements
    :returns: a list object

    """
    return [item for sublist in nested_list for item in sublist]


def with_magic(nested_list):
    """Dismount a nested list in one simples list

    >>> with_magic([[1,2,3], [4,5,6], [7,8,9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    It works with a map too:
    >>> with_magic(map(lambda x: [x], range(10)))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :nested_list: a list object with another lists as elements
    :returns: a list object

    """
    return list(itertools.chain(*nested_list))
