
from datetime import date
with open("dates.txt") as f:
    lines = f.readlines()   # f represents file with data
    lines = [int(l) for l in lines]
t = date.today()  # t represents today
for l in lines:  # l represents line
    d1 = date.fromtimestamp(l)
    td = d1-t  # td represents today's date
    print "%s is happening in %s days" % (d1, td.days)

