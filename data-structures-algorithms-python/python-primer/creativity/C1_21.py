def reverse_output():
    '''Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).
    '''
    x = ' '
    counter = 0
    while True:
        try:
            x += input('Line [{}]: '.format(counter))
            counter += 1
        except EOFError:
            return x[::-1]
