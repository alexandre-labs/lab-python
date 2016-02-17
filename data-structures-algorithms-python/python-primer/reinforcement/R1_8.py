'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?

Example:
s = 'Python'
len(s) = 6
-6 <= k < 0 -> let's suppose that k is 2.
j >= 0

s[-2] = 'o'
s[j] = 'o' if j == 4
'''
