#!/usr/bin/python3

from board_driver_simulator import open, close, det, set_port, get_port
import time 

'''
5.
Zmodyfikować funkcję get_key tak aby korzystała z portu wejściowego.
W funkcji powinno znajdować się tyko jedno wywołanie funkcji
get_port. Funkcja powinna używać przesunięcia binarnego. 
Test:  Program zapalający diodę odpowiadającą naciśnietemu przyciskowi. 
'''

def set_point(position):
	if position==0:
		set_port(1<<13)
	elif position==1:
		set_port(1<<5)
	elif position==2:
		set_port(1<<9)
	elif position==3:
		set_port(1<<17)
	else:
		set_port(0)

def get_key():
	port_state=get_port()
	if port_state&(1<<18):
		return 0
	elif port_state&(1<<12):
		return 1
	elif port_state&(1<<15):
		return 2
	elif port_state&(1<<20):
		return 3
	else:
		return -1

try: 
	open()  
#---------------------     
	while(True):
		set_point(get_key())
#--------------------- 
finally: 
	close() 
