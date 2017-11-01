
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


caller={}
for i in calls:
    caller.setdefault(i[0],0)
    caller[i[0]]+=int(i[3])
    caller.setdefault(i[1],0)
    caller[i[1]]+=int(i[3])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    max(caller, key=caller.get),
    caller[max(caller, key=caller.get)]))






