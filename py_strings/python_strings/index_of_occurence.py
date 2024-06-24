'''
A program that queries the user for strings A and B. The program then proceeds 
to find the index of the second occurrence of string B in string A.

'''

A = input ('Please enter a sentence: ')
B = input ('Please input any word in the sentence entered: ')
position_1 = A.find(B)
position_2 = A.find(B)+1
print (A.find((B), position_2))
