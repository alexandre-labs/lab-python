from curses import ascii


def remove_punctuation(string):
    '''Write a short Python function that takes a string
    s, representing a sentence, and returns a copy of
    the string with all punctuation removed. For exam-
    ple, if given the string "Lets try, Mike.", this function
    would return "Lets try Mike".
    >>> remove_punctuation('Lets try, Mike.')
    'Lets try Mike'
    >>> remove_punctuation('OMG!, this is really amazing! @.@')
    'OMG this is really amazing '
    '''
    return ''.join([l for l in string if ascii.isalnum(l) or ascii.isblank(l)])
