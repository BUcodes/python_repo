'''
A program that queries the user for number, and proceeds to output whether the number
is an even or an odd number. Program keeps asking more and more numbers and terminates
when the user enters a zero.
'''
# States user input as either odd or even until user enters 0
i = True
while i:
  number = int (input ('Enter number or zero to quit: '))
  if number == 0:
    i = False
    print ('Bye!')
    break
  if number % 2 == 0:
    print ('Your entered an even number')
  else: 
    print ('You entered an odd number')