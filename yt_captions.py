from youtube_transcript_api import YouTubeTranscriptApi
import sys
import time
import math

#

def find(search, captions):
    ar = []
    for cc in captions:
        if search in cc['text']:
            ar.append(cc)
    return ar

def fetch(rfile, query):
    wfile = input('name of saved transcripts file \n') + '.txt'
    #wfile = 'allagp.txt'

    ids = open(rfile, 'r').read().splitlines()

    #clean
    try:
        ids = [c[c.index('=')+1:] for c in ids]
    except:
        pass

    captions = []

    start = time.time()

    for i in ids:
        try:
            cc = YouTubeTranscriptApi.get_transcript(i)
            captions.append({i:cc})
            open('captions\\' + wfile, 'a').write(str({i:cc}) + '\n')
            print('wrote', i)
            found = find(query, cc)
            if len(found) > 0:
                print(found)
                print('https://youtube.com/watch?v=' + i + '&t=' + str(math.floor(found[0]['start'])))
        except Exception as e:
            print('error on ' + i)
    ##        print(e)
            pass

    print('elapsed: ' + str(time.time()-start))

if len(sys.argv) != 4:
    print('python yt_captions.py OPTION FILE QUERY')
    print('python yt_captions.py search transcript_file search_query')
    print('python yt_captions.py fetch ytID_file search_query')
    sys.exit()

if sys.argv[1] == 'fetch':
    fetch(sys.argv[2], sys.argv[3])

if sys.argv[1] == 'search':
    with open(sys.argv[2], 'r') as caption_file:
        captions = caption_file.read().splitlines()[:-1]
        captions = [eval(c) for c in captions]
        for caption in captions:
            ids = [i for i in caption]
            for i in ids:
                results = find(sys.argv[3], caption[i])
                if len(results) > 0:
                    print(results)
                    for r in results:
                        print('https://youtube.com/watch?v=' + i + '&t=' + str(math.floor(r['start'])))
