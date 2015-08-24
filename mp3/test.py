import sys, subprocess, urllib
import argparse

def getSpeech(phrase):
    if phrase == '123':
        return './mp3/'+'123.wav'    
    elif phrase == 'R2D':
        return './mp3/'+'R2D.mp3'
    else: 
        return '-h'
    
def raspberryTalk(text): # This will call mplayer and will play the sound
    subprocess.call(["mplayer",getSpeech(text)], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    raspberryTalk('R2D')
