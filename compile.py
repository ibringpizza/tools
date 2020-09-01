import os, sys

if len(sys.argv) != 3:
    print('python compile.py DIR OUTPUT_FILE')
    sys.exit()

os.chdir(sys.argv[1])

if not os.path.exists('compilation'):
    os.mkdir('compilation')

for file in os.listdir():
    if not os.path.exists(f'compilation/done_{file}'):
        #convert all videos to 1280x720, stereo, 48 kHz, and 30 fps. bitrates and data rates can differ -> https://trac.ffmpeg.org/wiki/AudioChannelManipulation
        #https://superuser.com/a/1136305
        #https://video.stackexchange.com/a/21098
        #https://trac.ffmpeg.org/wiki/ChangingFrameRate, https://trac.ffmpeg.org/wiki/FilteringGuide
        os.system(f'ffmpeg -i {file} -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=fps=30" -ac 2 -c:a aac -ar 48000 compilation/done_{file}')

os.chdir('compilation')

files = [f for f in os.listdir() if os.path.isfile(f)]

s = ''.join([f'[{_}:v:0][{_}:a:0]' for _ in range(len(files))])
#combine all videos -> https://trac.ffmpeg.org/wiki/Concatenate
cmd = f'ffmpeg -i {" -i ".join(files)} -filter_complex "{s}concat=n={len(files)}:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" {sys.argv[2]}'
print(cmd)
os.system(cmd)
