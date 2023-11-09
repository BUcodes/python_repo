'''
A program that queries the user for a space-seperated two-word string then outputs the latter word

'''
# request user input
input_word = input ('Please enter two words seperated with a space: ')
# find blank space between seperate words
space = input_word.find(' ')
# locate next position after space
position = space + 1
# assign second word to variable
second_word = input_word [position:]
print(second_word)