'''
This is a simple program that queries a string from the user, and proceeds to output the total number of vowels in it (a,e,i,o,u).

-Assumumption: the string only contains lowercase characters

'''
# request user input
string = input ('Please enter a word in small letters: ')
a = string.count ('a')
b = string.count ('e')
c = string.count ('i')
d = string.count ('o')
e = string.count ('u')
vowels = a + b + c + d + e
print (vowels)