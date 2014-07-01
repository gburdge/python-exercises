i1 = int(raw_input("Enter a number: "))
i2 = int(raw_input("Enter a number: "))

print i1 + i2
print i1 - i2
print i1 * i2
print str(i1 / i2) + " remainder " + str(i1 % i2)
# i1 = [1, 2, 3]
# i1 = tuple(i1)
# print i1
# print type(i1)



# QUESTION 1
#  What happens when you try to divide by zero when you run your program? Get error:
# ZeroDivisionError: integer division or modulo by zero
# QUESTION 2
# What happens when you multiply two VERY LARGE integers?
# It doesn't use scientific notation and it does the math without any errors.
# QUESTION 3
# What happens when you enter a letter instead of a number at the prompt?
# I get an error message that says:
# ValueError: invalid literal for int() with base 10: 'dfff'