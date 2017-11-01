
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

num=set()

for nums in calls:
    num.add(nums[0])
    num.add(nums[1])
for nums in texts:
    num.add(nums[0])
    num.add(nums[1])

print("There are {} different telephone numbers in the records.".format(len(num)))
