# Programming Project #1 - Arithmetic

from sys import exit

num1_string = raw_input('Please enter the first integer: ')
num2_string = raw_input('Please enter the second integer: ')

# We will have a problem casting if either entry is not a number
# We want to abort completely if there is something other than a number
if num1_string.isalpha() or num2_string.isalpha():
        print "Both integers should be numbers, not something else!"
        exit()

num1 = int(num1_string)
num2 = int(num2_string)

# We will have a problem if we divide by 0
# Checking the second integer to make sure it is not 0
if num2 == 0:
        print "The second number would cause a divide by zero exception!"
        exit()

print "The sum of %d and %d is: %d" %(num1, num2, num1 + num2)
print "The difference of %d and %d is: %d" %(num1, num2, num1 - num2)
print "The product of %d and %d is: %d" %(num1, num2, num1 * num2)
print "The quotient of %d and %d is: %d with remainder %d" %(num1, num2, num1 / num2, num1 % num2)