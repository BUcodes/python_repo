'''
A program that queries the user for a number N, and then proceeds to output all powers of two smaller than N.

For example:
- if N is given a value 9, numbers 1, 2, 4, and 8 are output (20, 21, 22, 23)
'''

# Task 3: Outputs all power of 2 smaller than user input
N = int (input ('Enter a number: '))
for i in range (0, N):
  if 2**i < N:
    print (2**i)