'''
Write a program that queries the user for strings A and B, and proceeds to output 
whether B is a permutation of A. To confirm this, the following conditions need to be met:

1. There is an equal amount of characters in A and B (or, the length of A is equal to length
of B)
2. For every character found in A, there is an equal amount of same character in B.

For example:

- ”ABBA”, ”BAAB” and ”ABAB” are all permutations of string ”AABB”
- ”elvis” and ”lives” are permutations of string ”ilves”
'''



# Check if two user inputs are anagrams
a = input ('Enter string A: ')
b = input ('Enter string B: ')
for i in a,b:
  ia = a.count(i)
  ib= b.count(i)
if ia == ib and len(a) == len(b):
  print (a, 'is a permutation of', b)
else:
  print (a, 'is not a permutation of', b)
