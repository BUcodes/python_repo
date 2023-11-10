''' 
A program that queries the user for a number N, and then proceeds to output all numbers
between -N and N.

'''

# Task 1: Outputs user input in a range of negative to positive values.
N = int(input ('Enter a number: '))
N_range = [i for i in range (-N, N+1)]
print (N_range)
