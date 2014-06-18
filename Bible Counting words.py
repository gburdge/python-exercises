# Counts the number of words in the bible from "Bible.txt" file
# Sorts the results in reversed sorted words
# Prints the results
from collections import defaultdict
from operator import itemgetter

word_counts = defaultdict(int)

with open('bible.txt') as f:
    for line in f:
        line = line.split()
        for word in line:
            word_counts[word.lower()] += 1

word_counts = reversed(sorted(word_counts.iteritems(), key=itemgetter(1)))

for t in word_counts:
    print t