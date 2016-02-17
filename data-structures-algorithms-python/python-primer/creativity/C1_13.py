'''
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.


Without to use recursion (I know...recursion is cool, but not in Python....
    let's imagine a infinit list? Maybe in Haskell...=P)
define x as the list length;
define a new empty list called 'result'
while x is greater than 0:
    get item in position -1 on the list;
    add this item in the 'result';
    remove this item from the first list;
    the value of x is the current x's value - 1

in the real world
foo = [1,2,3,4,5,5]
# foo reversed
foo[::-1]
'''
