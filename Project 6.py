# Program to Write 10 random strings to file
# Read them in from file then count number of characters
# Counting # of characters and their frequency, then output each char and its count
# Output each character with string and list indicating output of

import random
import string
from collections import defaultdict

def generate_strings():
    """This function writes ten random strings to a file called project_six.dat"""

    with open("project_six.dat", 'w') as f:
        for i in range(0, 10):
            random_string = ''.join([random.choice(string.ascii_letters)
                                     for n in range(32)])
            f.write(random_string + '\n')
 

def count_characters(line):
    character_count = defaultdict(int)

    for char in line:
        if char != '\n':
            character_count[char] += 1

    return character_count

    # Alternate method without using defaultdict
    # character_count = {}
    # for char in line:
    #     if char in character_count:
    #         character_count[char] += 1   <-- we are seeing character again, increment
    #     else:
    #         character_count[char] = 1    <-- first time we've seen the character so count it once


def print_file():
    with open("project_six.dat") as f:  # Use file to refer to the file object
        for line in f:
            counted_characters = count_characters(line)
            print line,
            for key, value in counted_characters.items():
                print key + ' => ' + str(value) + ' ',
            print '\n'
            # print counted_characters  # print line from file created as f

generate_strings()
print_file()

