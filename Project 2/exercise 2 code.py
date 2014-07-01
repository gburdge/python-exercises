from sys import exit

gallons_string = raw_input('Please enter the number of gallons of gasoline: ')

# We want to abort completely if there is something other than a number
if gallons_string.isalpha():
        print "Gallons should be entered as a number, not something else!"
        exit()

gallons = int(gallons_string)

# We will have a problem if we divide by 0
if gallons == 0:
        print "Gallons should NOT be zero!"
        exit()

liters = gallons * 3.7854
barrels = gallons / 19.5
c02 = gallons * 20
ethanol = (gallons * 115000) / 75700
cost = gallons * 4

print "%f gallon(s) is the equivalent of %f liters" %(gallons, liters)
print "%f gallon(s) of gasoline requires %f barrels of oil" %(gallons, barrels)
print "%f gallon(s) of gasoline produces %f pounds of C02" %(gallons, c02)
print "%f gallon(s) of gasoline is energy equivalent to %f gallons of ethanol" %(gallons,
ethanol)
print "%f gallon(s) requires %f US dollars" %(gallons, cost)