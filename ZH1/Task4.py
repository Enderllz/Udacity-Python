import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

possible_phone_list = [x[0] for x in calls]
impossible_phone_list = sum([[x[0], x[1]] for x in texts], []) + [x[1] for x in calls]
telemarketers = sorted(set(possible_phone_list) - set(impossible_phone_list))

print("These numbers could be telemarketers: ")
for x in telemarketers:
    print(x)