#!/usr/bin/python3

from board_driver_simulator import open, close, det, set_port, get_port, pot
import time 

'''
Napisać funkcję get_pot działającą tak samo jak funkcja pot ale
korzystającą z portu wejściowego.
Test: Program wyświetlający na ekranie stan potencjometru w kodzie
binarnym a następnie dziesiętnym. Działanie
programów sprawdzić obracając potencjometrem. 

'''

def get_pot():
	port_state=get_port()
	for i in range(10):
		maska=1<<i
		if port_state&maska:
			return port_state

try: 
	open()  
#---------------------     
	while(True):
		my_pot=get_pot()
		print(my_pot)
#--------------------- 
finally: 
	close() 
