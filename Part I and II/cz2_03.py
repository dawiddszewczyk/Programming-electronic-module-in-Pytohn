#!/usr/bin/python3

'''
3.
Funkcja step() przesuwająca punkt świetlny o jeden ‘w górę’ modulo 4. Przykład 
step
() # 0->1  
step
() # 1->2  
... 
step
() # 3->0 
Test 1: Program przesuwający punkt świetlny 
Test 2: Program przesuwający punkt świetlny, jeżeli na
ciśnieto przycisk 0. 
'''

from board_driver_simulator import open,close,but,pot,det,led
import time

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

def step():
	global vstep
	vstep+=1
	vstep%=4
	led(set_point(vstep))

try:
	open()
#---------------------
	led(0)
	while(True):
		#test1
		#step()

		#test2
		if get_key()==0:
			step()
		#time.sleep(0.5)	
#---------------------
finally:
	close()
