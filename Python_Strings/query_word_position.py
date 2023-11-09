# A program that queries a string and then outputs the second to last character as many times as the length of the string

word = input ('Please enter a word: ')
print (word[-2] * len(word))