# sequence = [1,2,3,4,5,6]
def code_fragment(sequence):
    '''Give an example of a Python code fragment that attempts
     to write an element to a list based on an index that
     may be out of bounds. If that index is out of bounds,
     the program should catch the exception that results, and
    print the following error message:
    "Don’t try buffer overflow attacks in Python!"
    '''
    try:
        sequence[10] = 'Attack!'
    except Exception:
        raise IndexError("Don't try buffer overflow attacks in Python!")
