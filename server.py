#!/usr/bin/env python
#!coding=utf-8

import logging
import time
import os
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import threading
import signal
import serial

import sys, subprocess, urllib
def getSpeech(phrase):
    if phrase == '123':
        return '/home/pi/rapiro/mp3/'+'123.wav'
    elif phrase == 'R2D':
        return '/home/pi/rapiro/mp3/'+'R2D.mp3'
    elif phrase == 'sound1':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-1.mp3'   
    elif phrase == 'sound2':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-2.mp3'
    elif phrase == 'sound3':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-3.mp3'
    elif phrase == 'sound4':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-4.mp3'
    elif phrase == 'sound5':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-5.mp3'
    elif phrase == 'sound6':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-6.mp3'
    elif phrase == 'sound7':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-7.mp3'
    elif phrase == 'sound8':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-8.mp3'
    elif phrase == 'sound9':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-9.mp3'
    elif phrase == 'sound10':
        return '/home/pi/rapiro/mp3/'+'r2d2+sound-10.mp3'

def raspberryTalk(text): # This will call mplayer and will play the sound
    
    subprocess.call(["mplayer",getSpeech(text)], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

HTTP_PORT = 8000
WEBSOCKET_PORT = 9099

class CommandWebsocket(WebSocket):

	def handleMessage(self):
		print self.data, 'from', self.address
		self.sendMessage(str(self.data))

		if self.data == 'robot':
			connection = '/dev/ttyAMA0'
                        ser = serial.Serial(connection, 57600, timeout=10)
                        ser.write("#M9")
			raspberryTalk('sound1')
		elif self.data == 'body' or self.data == 'voice_go':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#M1")
			raspberryTalk('sound2')
		elif self.data == 'voice_back':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#M2")
			raspberryTalk('sound3')
		elif self.data == 'voice_left':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#M3")
			raspberryTalk('sound4')
		elif self.data == 'voice_right':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#M4")
			raspberryTalk('sound5')
		elif self.data == 'left':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write('#PS05A080T010#PS02A000T010#PS07A110T003\
				#PS07A070T010#PS07A110T010')
			raspberryTalk('sound6')
		elif self.data == 'right':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write('#PS05A180T010#PS02A100T010#PS04A070T010\
				#PS04A110T03#PS04A070T010')
			raspberryTalk('sound7')
		elif self.data == 'orange':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#PR237G100B024T010")
			#raspberryTalk('sound8')
		elif self.data == 'green':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#PR000G255B000T010")
			#raspberryTalk('sound9')
		elif self.data == 'blue':
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write("#PR000G000B255T010")              
			#raspberryTalk('sound10')
		elif self.data == 'shake':
                        connection = '/dev/ttyAMA0'
                        ser = serial.Serial(connection, 57600, timeout=10)
                        ser.write('#PS00A080T002#PS00A110T002#PS00A080T002\
                                   #PS00A110T002#PS00A080T002#PS00A110T002\
                                   #PS00A080T002#PS00A110T002')
			raspberryTalk('R2D')                 
		elif self.data == 'slam':
                        connection = '/dev/ttyAMA0'
                        ser = serial.Serial(connection, 57600, timeout=10)
                        ser.write('#PS00A040T005#PS00A090T005#PS00A040T005\
                                   #PS00A090T005#PS00A040T005#PS00A090T005\
                                   #PS00A040T005#PS00A090T005')
			raspberryTalk('sound4')
		elif self.data == 'pickup':
                        connection = '/dev/ttyAMA0'
                        ser = serial.Serial(connection, 57600, timeout=10)
                        ser.write('#PS02A000T050#PS03A000T050#PS04A000T050\
                                   #PS02A180T050#PS03A180T050#PS04A180T050')
			raspberryTalk('sound5')
		else:
			connection = '/dev/ttyAMA0'
			ser = serial.Serial(connection, 57600, timeout=10)
			ser.write('#M0')

	def handleConnected(self):
		print self.address, 'connected'
		raspberryTalk('R2D')

	def handleClose(self):
		print self.address, 'closed'
		raspberryTalk('R2D')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/www')
    SocketServer.TCPServer.allow_reuse_address = True
    httpserver = SocketServer.TCPServer(
        ('', HTTP_PORT), SimpleHTTPRequestHandler)
    print('http server port: %d' % HTTP_PORT)
    httpd = threading.Thread(target=httpserver.serve_forever)
    httpd.start()
    websocket = SimpleWebSocketServer('', WEBSOCKET_PORT, CommandWebsocket)

    def close_sig_handler(signal, frame):
        httpserver.shutdown()
        httpd.join()
        websocket.close()
	
	connection = '/dev/ttyAMA0'
        ser = serial.Serial(connection, 57600, timeout=10)
        ser.write('#M0')

        print('quit')
        sys.exit()

    signal.signal(signal.SIGINT, close_sig_handler)

    websocket.serveforever()
