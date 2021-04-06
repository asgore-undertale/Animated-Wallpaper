#pip3 install opencv-python
#pip install ctypes
from ctypes import windll
from cv2 import VideoCapture, imwrite
from time import sleep
from os import walk, remove, path

frames_per_sec = 60

def dir_list(path): return [root+'/'+'{}{}'.format('', f) for root, dirs, files in walk(path) for f in files]

def getFrame(vid):
    print('Please wait...')
    vidcap = VideoCapture(vid)
    success,image = vidcap.read()
    count = 0
    while success:
        imwrite("frames\\frame %d.jpg" % count, image)     
        success,image = vidcap.read()
        count += 1

if input('New background? (y\\n): ') == 'y':
    for f in dir_list('frames\\'): remove(path.join('', f))
    getFrame(input('Enter the Mp4 file. (Only english and no spaces):\n'))

while True:
    for file in dir_list('frames\\'):
        if not file.endswith('.jpg'): continue
        windll.user32.SystemParametersInfoW(20, 0, file, 0)
        sleep(1/frames_per_sec)