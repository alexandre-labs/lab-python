def vowels_counter(string):
    '''Write a short Python function that counts the
    number of vowels in a given character string.
    '''
    return sum(list(set(string) & set(['a', 'e', 'i', 'o', 'u'])))
