#!/usr/bin/python3

from my_board import *
import time

'''
2.
Funkcja wait_for_key() oczekująca na naciśniecie
dowolnego przycisku. 
Test 1: Jakiś program z funkcją print 
Test 2: Program  obracający tarczę o 12 kroków w pra
wo po każdym naciśnięciu dowolnego przycisku. 
'''

try:
	open()
#---------------------
	led(0)
	while(True):
		#test1
		print(wait_for_key())
		
		#test2
		if wait_for_key()>=0:
			for i in range(12):
				step('right')
				time.sleep(0.25)
#---------------------
finally:
	close()
