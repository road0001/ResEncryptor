import os
import sys
import ctypes
import platform

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.

BACKGROUND_BLACK = 0x00 # black.
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_DARKGREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.


def isWindows():
	return 'Windows' in platform.system()

try:
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
except:
	std_out_handle = 0

def out(o):
	# print(o),
	sys.stdout.write(o)
	sys.stdout.flush()
def outln(o):
	print(o)

colorListF={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'cyan':36,'white':37}
colorListFW={\
	'black':FOREGROUND_BLACK,'red':FOREGROUND_RED,'green':FOREGROUND_GREEN,'yellow':FOREGROUND_YELLOW,'blue':FOREGROUND_BLUE,'purple':FOREGROUND_PINK,'cyan':FOREGROUND_SKYBLUE,'white':FOREGROUND_WHITE,\
	'dark_black':FOREGROUND_BLACK,'dark_red':FOREGROUND_DARKRED,'dark_green':FOREGROUND_DARKGREEN,'dark_yellow':FOREGROUND_DARKYELLOW,'dark_blue':FOREGROUND_DARKBLUE,'dark_purple':FOREGROUND_DARKPINK,'dark_cyan':FOREGROUND_DARKSKYBLUE,'dark_white':FOREGROUND_DARKWHITE,'dark_gray':FOREGROUND_DARKGRAY\
}

colorListB={'black':40,'red':41,'green':42,'yellow':43,'blue':44,'purple':45,'cyan':46,'white':47}
colorListBW={\
	'black':BACKGROUND_BLACK,'red':BACKGROUND_RED,'green':BACKGROUND_GREEN,'yellow':BACKGROUND_YELLOW,'blue':BACKGROUND_BLUE,'purple':BACKGROUND_PINK,'cyan':BACKGROUND_SKYBLUE,'white':BACKGROUND_WHITE,\
	'dark_black':BACKGROUND_BLACK,'dark_red':BACKGROUND_DARKRED,'dark_green':BACKGROUND_DARKGREEN,'dark_yellow':BACKGROUND_DARKYELLOW,'dark_blue':BACKGROUND_BLUE,'dark_purple':BACKGROUND_DARKPINK,'dark_cyan':BACKGROUND_DARKSKYBLUE,'dark_white':BACKGROUND_DARKWHITE,'dark_gray':BACKGROUND_DARKGRAY\
}

def outC(o,fc,bc,B):
	if isWindows():
		windows_colorText(o,False,fc,bc,B,B)
	else:
		oc='\033[%s;%s;%sm%s\033[0m' %(B,colorListF[fc],colorListB[bc],o)
		out(oc)
def outlnC(o,fc,bc,B):
	if isWindows():
		windows_colorText(o,True,fc,bc,B,B)
	else:
		oc='\033[%s;%s;%sm%s\033[0m' %(B,colorListF[fc],colorListB[bc],o)
		outln(oc)

def colorText(o,colf,colb,BF,BB):
	fd=''
	if not BF>=1:
		fd='dark_'
	bd=''
	if not BB>=1:
		bd='dark_'
	if isWindows():
		# Windows is not support change color in line
		# windows_setColor(colorListFW[fd+''+colf] | colorListBW[bd+''+colb])
		# windows_resetColor()
		return o
	else:
		return '\033[%s;%s;%sm%s\033[0m' %(BF,colorListF[colf],colorListB[colb],o)

def windows_setColor(color, handle=std_out_handle):
	if isWindows():
		Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
	else:
		Bool = False
	return Bool

def windows_resetColor():
	windows_setColor(FOREGROUND_DARKWHITE | BACKGROUND_BLACK)

def windows_colorText(o,ln,fcolor,bcolor,isflight,isblight):
	fd=''
	if not isflight>=1:
		fd='dark_'
	bd=''
	if not isblight>=1:
		bd='dark_'
	windows_setColor(colorListFW[fd+''+fcolor] | colorListBW[bd+''+bcolor])
	if ln:
		outln(o)
	else:
		out(o)
	windows_resetColor()

# styles = {
# 	'reset': '\x1B[0m',
# 	'bright': '\x1B[1m',
# 	'grey': '\x1B[2m',
# 	'italic': '\x1B[3m',
# 	'underline': '\x1B[4m',
# 	'reverse': '\x1B[7m',
# 	'hidden': '\x1B[8m',
# 	'black': '\x1B[30m',
# 	'red': '\x1B[31m',
# 	'green': '\x1B[32m',
# 	'yellow': '\x1B[33m',
# 	'blue': '\x1B[34m',
# 	'magenta': '\x1B[35m',
# 	'purple': '\x1B[35m',
# 	'cyan': '\x1B[36m',
# 	'white': '\x1B[37m',
# 	'blackBG': '\x1B[40m',
# 	'redBG': '\x1B[41m',
# 	'greenBG': '\x1B[42m',
# 	'yellowBG': '\x1B[43m',
# 	'blueBG': '\x1B[44m',
# 	'magentaBG': '\x1B[45m',
# 	'purpleBG': '\x1B[45m',
# 	'cyanBG': '\x1B[46m',
# 	'whiteBG': '\x1B[47m'
# }
# def color(keys=[], source=''):
# 	values = ''
# 	if isinstance(keys,str) and (keys in styles):
# 		values = styles[keys]
# 	if keys:
# 		for key in keys:
# 			values += styles[key]
# 	return '{}{}{}'.format(values,source,styles['reset'])

# def out(content='', textColor=[]):
# 	sys.stdout.write(color(textColor, content))
# 	sys.stdout.flush()
# def outln(content='',textColor=[]):
# 	out(content+'\n',textColor)

# # def includes(key,dic):
# # 	for k,v in dic:
# # 		pass