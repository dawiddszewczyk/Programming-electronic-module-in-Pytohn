#!/usr/bin/python3

from board_driver_simulator import open, close, det, set_port, get_port
import time 

'''
4. Zmodyfikować funkcję get_detector tak aby korzystała
z portu wejściowego. 
Test:  Dodać do testu z zadania 2 funkcjonalność polegającą
na wyświetlanie na ekranie napisu „bingo!” w momencie 
zrównania się markera z detektorem. 
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
		
def get_detector():
	maska=1<<30
	port_state=get_port()
	if port_state&maska:
		return 'active'
	return 'no_active'

try: 
	open()  
#---------------------     
	while(True):
		set_point(0)
		if get_detector()=='active':
			print('bingo!')
		set_point(1)
		if get_detector()=='active':
			print('bingo!')
		set_point(2)
		if get_detector()=='active':
			print('bingo!')
		set_point(3)
		if get_detector()=='active':
			print('bingo!')
#--------------------- 
finally: 
	close() 
