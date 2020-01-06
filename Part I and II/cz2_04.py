#!/usr/bin/python3

'''
4. Modyfikacja funkcji step pozwalająca na określenie kierunku 
przesunięcia:
step(‘right’) # 0->1
step(‘right’) # 1->2
step(‘left’) # 2->1
step(‘left’) # 1->0
Test 1: Program: obracający krążkiem w lewo jeżeli naciśnieto 
przycisk ‘0’ a w prawo jeśli naciśnieto przycisk ‘1’
'''

from board_driver_simulator import open,close,but,pot,det,led

vstep=0

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

def step(direction):
	global vstep
	if direction=='right':
		vstep+=1
	elif direction=='left':
		vstep-=1
	vstep%=4
	led(set_point(vstep))

try:
	open()
#---------------------
	led(0)
	while(True):
		if get_key()==0:
			step('left')
		elif get_key()==1:
			step('right')	
#---------------------
finally:
	close()
