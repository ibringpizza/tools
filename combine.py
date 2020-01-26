import sys
import os

def combine(path):
    os.chdir(path)
    for f in os.listdir():
        r = open(f, 'r').read().splitlines()
        open('--combined--.txt','a').write('\n'.join(r) + '\n')

if len(sys.argv) != 2:
    print('python combine.py DIRPATH')
    sys.exit()
    
path = sys.argv[1]
combine(path)
