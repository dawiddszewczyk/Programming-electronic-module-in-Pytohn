#!/usr/bin/python3

'''
12. Program wyświetlający na ekranie stan potencjometru (w kodzie
dziesiętnym). Działanie programu sprawdzić obracając potencjometrem.
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		print(pot())	
#---------------------
finally:
	close()
