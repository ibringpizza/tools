import sys
import operator
import re

if len(sys.argv) != 5 and sys.argv[1] != 'head':
    print('python csv.py file.csv [column] [acending (a)/descending (d)] [itemstodisplay]')
    print('python csv.py head file.csv')
    sys.exit()

if sys.argv[1] == 'head':
    with open(sys.argv[2], 'r') as o:
        for _ in range(10):
            print(o.readline())
    sys.exit()
#regex - https://stackoverflow.com/a/2701015
#https://stackoverflow.com/a/3513858

lines = open(sys.argv[1], 'r').read().splitlines()
ready = [re.compile(',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)').split(line) for line in lines]
for L in range(len(ready)):
    for i in range(len(ready[L])):
        try:
            ready[L][i] = float(ready[L][i])
        except Exception as e:
            pass

try:
    ready = sorted(ready, key=operator.itemgetter(int(sys.argv[2])), reverse=(sys.argv[3]=='d'))
except:
    print([r for r in ready if len(r) == min([len(r) for r in ready])])
    print(sorted([len(r) for r in ready]))

for line in ready[:int(sys.argv[4])]:
    print(','.join([str(i) for i in line]))
