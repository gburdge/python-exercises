BARLEYCORNS_IN_METERS = 117.647
ONE_FURLONG_IN_YARDS = 220
ONE_METER__IN_FURLONGS = 201.170
HOURS_IN_DAY = 24.0
METERS_IN_MILE = 1609.344
YARDS_IN_MILE = 1760
DAYS_IN_FORTNIGHT = 14
FEET_IN_ONE_MILE = 5280
MACH_IN_MILES_PER_HOUR = 767.71
ONE_FURLONG_PER_HOUR = 2688
SPEED_OF_LIGHT_PER_HOUR = 1.491 * 10**-9

miles = float(raw_input("Please, enter a value for speed in miles per hour: "))
print "Original speed in mph: %.1f" % miles

num_barleycorn = (miles * METERS_IN_MILE * BARLEYCORNS_IN_METERS) * HOURS_IN_DAY
num_furlongs = miles * ONE_FURLONG_PER_HOUR
num_mach = (miles / MACH_IN_MILES_PER_HOUR)
num_speed_of_light = miles * SPEED_OF_LIGHT_PER_HOUR

print "Converted to barleycorn/day is: %f" % num_barleycorn
print "Converted to furlongs/fortnight is: %f" % num_furlongs
print "Converted to Mach number is: %f" % num_mach
print "Converted to Percentage of Speed of Light is: %e" % num_speed_of_light

# print "%.1f gallons is the equivalent of %f liters" % (num_gallons, num_liters)
# print "%.1f gallons requires %f barrels" % (num_gallons, num_barrels)
# print "%.1f gallons produces %f pounds of CO2" % (num_gallons, num_pounds_CO2)
# print "%.1f gallons produces %f BTUs" % (num_gallons, num_btus)
# print "%.1f gallons cost %f dollars" % (num_gallons, num_dollars)