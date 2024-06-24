'''
A program that queries the user for a number and proceeds to output whether or not the number is a prime number.
A prime number is a number that has exactly two natural number (number > 0) divisors: one and the number itself. 
Thus, the ten smallest prime numbers are 1, 2, 3, 5, 7, 11, 13, 17, 19 and 23 as any of the cannot be evenly 
divided by other numbers than one and the number itself.
'''

# Examines user input if a prime number or not
a = int (input ('Enter a number: '))
for i in range (1, a):
  if a % i != 0:
    print (a, 'is a prime number')
  else:
    print(a, 'is not a prime number')
  break
if a == 1:
  print (a, 'is a prime number')
if a == 0:
  print ('Please enter a natural number')
