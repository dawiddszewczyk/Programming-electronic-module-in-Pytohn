#!/usr/bin/python3

'''
1. Napisać program który będzie na przemian zapalał i gasił 
diodę świecącą numer 0
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		led(0)
		led(1)
#---------------------
finally:
	close()
