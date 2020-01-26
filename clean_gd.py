#clean json files from ftp.godaddy.com by setting a maximum bid amount to be returned

import sys
import json

def clean(path, maxb):
    j = json.loads(open(path, 'r', errors='ignore').read())
    ar = []
    for e in j['data']:
        if e['numberOfBids'] <= maxb:
            ar.append(e['domainName'] + ',' + str(e['valuation'][1:]).replace(',','') + ',' + str(e['numberOfBids']))
    open('cleaned_' + path[max(path.rfind('/'),path.rfind('\\'),path.rfind('//'))+1:], 'a').write('\n'.join(ar))

if len(sys.argv) < 3:
    print('Provide file path in following format: python clean_gd.py -u PATH MAXBIDS')
    sys.exit()

path = sys.argv[sys.argv.index('-u')+1]
maxb = int(sys.argv[-1])

clean(path, maxb)
