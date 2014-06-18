CURRENT_POPULATION = 307357870
BIRTHS_PER_YEAR = 4505133
DEATHS_PER_YEAR = 2425846
NEW_IMMIGRANTS_PER_YEAR = 901029
POPULATION_CHANGE = BIRTHS_PER_YEAR + NEW_IMMIGRANTS_PER_YEAR - DEATHS_PER_YEAR

years = int(raw_input("Please, enter an integer representing the number of years: "))

print "In %s years, the population will change by %s to be %s" % (years, POPULATION_CHANGE * years,
                                                                  POPULATION_CHANGE * years + CURRENT_POPULATION)



