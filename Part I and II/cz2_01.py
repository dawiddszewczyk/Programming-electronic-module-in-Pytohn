#!/usr/bin/python3

'''
1. Napisać funkcję set_point(position), która zaświeci diodę świecącą
o zadanej pozycji (od 0 do 3).  Pozostałe diody powinny być zgaszone.  
Podanie argumentu z poza zakresu 0-3 powinno skutkować zgaszeniem 
wszystkich diod. Użyć sekwencji if,elif,elif..  
Test: Program zapalający diodę odpowiadającą naciśnietemu przyciskowi.
'''

from board_driver_simulator import open,close,but,pot,det,led

def set_point(position):
	if position==0:
		return 1
	elif position==1:
		return 2
	elif position==2:
		return 4
	elif position==3:
		return 8
	else:
		return 0

try:
	open()
#---------------------
	led(0)
	while(True):
		but_state=but()
		if(but_state==1):
			led(set_point(0))
		elif(but_state==2):
			led(set_point(1))
		elif(but_state==4):
			led(set_point(2))
		elif(but_state==8):
			led(set_point(3))
		else:
			led(set_point(-1))
#---------------------
finally:
	close()
