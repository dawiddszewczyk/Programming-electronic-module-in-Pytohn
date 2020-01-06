#!/usr/bin/python3

'''
13. Program pozwalający na ustawianie potencjometrem pozycji punktu
świetlnego. Wykorzystać cały zakres potencjometru.
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		pot_state=pot()
		if pot_state in range(1, 250):
			led(1)
		elif pot_state in range(251, 500):
			led(2)
		elif pot_state in range(501, 750):
			led(4)
		elif pot_state in range(751, 1000):
			led(8)
		else:
			led(0)	
#---------------------
finally:
	close()
