''' 
A program that queries two strings from the user. The program then replaces all the occurrences of the second string from the first string, surrounded by quotes

'''
# Request user inputs
first_input = input ('Please enter a word: ')
second_input = input ('Please enter any letter from the first word: ')

# replace and print all occurrences of the second string from the first string, surrounded by quotes
print (first_input.replace(second_input,  f'"{second_input}"'))