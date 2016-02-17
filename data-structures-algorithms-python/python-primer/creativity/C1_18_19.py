'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

cp = current position

list[cp + 1](2) - cp(0) == 2

list[cp +1](6)  - cp(2) == 4

list[cp +1](12) - cp(6) == 6

list[cp +1](20) - cp(12) == 8

list[cp + 1](30)- cp(20) == 10

"Second-order arithmetic"
...
'''

'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.

[chr(x) for x in range(ord('a'), ord('z') +1)]
'''
