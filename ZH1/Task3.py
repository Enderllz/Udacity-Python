import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)





called_list = [x for x in calls if x[0][:5] == "(080)"]

def get_code(x):
  if x[:3] == "140":
    return "140"
  elif x[5] == " ":
    return x[:4]
  else:
    return x[: x.index(")") + 1]

code_set = set(map(get_code, set([x[1] for x in called_list])))
print("The numbers called by people in Bangalore have codes:")
for code in sorted(code_set):
  print(code)

b_b_list = [x for x in called_list if x[1][:5] == "(080)"]
percentage = len(b_b_list) / len(called_list) * 100
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

"""
list_caller={}
for i in calls:
    list_caller.setdefault(i[0],[]).append(i[1])

called=[]
called_wewant=[]
for key in list_caller:
    if key[:5] =="(080)":
        called.append(list_caller[key])
for key in called:
    called_wewant+=key
list_called=list(set(called_wewant))

call_code=[]
for m in list_called:
    if m[0]=="(":
        for i in range(0,10):
            if m[i]==")":
                call_code.append(m[0:i+1])
    else:
        call_code.append(m[0:4])

call_code_only=list(set(call_code))
call_code_only.sort()
print("The numbers called by people in Bangalore have codes:")
for i in call_code_only:
    print(i)

call_code_080=[]
for m in called_wewant:
    if m[0]=="(" and m[1]=="0" and m[2]=="8" and m[3]=="0" and m[4]==")":
        call_code_080.append(m)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("%.2f%%" % (float(len(call_code_080))/len(called_wewant)*100)))
"""





