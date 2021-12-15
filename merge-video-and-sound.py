import os
from os import listdir
from os.path import isfile, join

mypath = '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
mp4s = [f.split('.')[:-1] for f in onlyfiles if f.split('.')[-1] == 'mp4']


def path_creator(string):
    string = string.replace(' ', '\ ')
    string = string.replace('#', '\#')
    string = string.replace('&', '\&')
    return string


for f in mp4s:
    os.system(
        f'ffmpeg -i ./{path_creator(str(*f))}.mp4 -i ./{path_creator(str(*f))}.webm -c copy ../{path_creator(str(*f))}.mp4')
