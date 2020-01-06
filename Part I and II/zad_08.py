#!/usr/bin/python3

'''
8. Zmodyfikować program tak aby wyświetlał stan przycisków w
postaci binarnej a następnie heksadecymalnej
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		print(bin(but()))
		print(hex(but()))
#---------------------
finally:
	close()
