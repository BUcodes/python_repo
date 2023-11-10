'''
A program that queries the user for a string, and proceeds to generate a new string with
all of the letters from the original string that are in upper case. This generated string is then
output. You can assume that the string given does not contain characters other than letters (e.g.
numbers or spaces)
'''

# Extract uppercase letters from user input
user = input ('Enter a word that contains both capital and small letters: ')
upper_cases= ""
for i in user:
 if i.isupper():
   upper_cases = upper_cases + i
print (upper_cases)