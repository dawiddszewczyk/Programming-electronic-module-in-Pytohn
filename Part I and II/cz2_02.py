#!/usr/bin/python3

'''
2. Funkcja get_key(), zwracająca informację o numerze naciskanego
przycisku (0-3). Jeżeli żaden  przycisk  nie jest  naciśniety lub
jeżeli  naciśniety jest  więcej  niż jeden  przycisk  funkcja
powinna  zwracać wartość ‘-1’.  
Test 1: Program wyświetlający numer naciśnietego przycisku. 
Test 2: Test z punktu 1 - uzycie funkcji set_point
'''

from board_driver_simulator import open,close,but,pot,det,led

def get_key():
	but_state=but()
	if but_state==1:
		return 0
	elif but_state==2:
		return 1
	elif but_state==4:
		return 2
	elif but_state==8:
		return 3
	else:
		return -1

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
		#test1
		print(get_key()) 	
		#test2		
		led(set_point(get_key()))	
#---------------------
finally:
	close()
