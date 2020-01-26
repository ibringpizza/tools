import sys
import math

def remove(path):
    d = {}
    ar = open(path, 'r').read().splitlines()
    size = math.ceil(len(ar)*2.5)
    for a in ar:
        index = hash(a)%size
        if index in d and d[index] != None:
            if a in d[index]:
                continue
            d[index].append(a)
        else:
            d[index] = [a]
    done = []
    
    for i in d:
        for line in d[i]:
            done.append(line)
    open('dup-removed_' + path[max(path.rfind('/'),path.rfind('\\'),path.rfind('//'))+1:], 'w').write('\n'.join(done))


if len(sys.argv) != 2:
    print('python remove_duplicates.py FILE')
    sys.exit()

remove(sys.argv[1])
