#!/usr/bin/python3

from my_board import *
import time

'''
3.
Modyfikacja funkcji steps, pozwalająca na określenie
liczby kroków do wykonania. 
Test 1: Program, z pętlą główną jak poniżej:  
while(True): 
steps(‘right’,6); time.sleep(0.5) 
steps(‘right’,12); time.sleep(0.5) 
steps(‘right’,12); time.sleep(0.5) 
steps(‘right’,6); time.sleep(0.5) 
'''

try:
	open()
#---------------------
	while(True): 
		steps('right',6); time.sleep(0.5) 
		steps('right',12); time.sleep(0.5) 
		steps('right',12); time.sleep(0.5) 
		steps('left',6); time.sleep(0.5) 
#---------------------
finally:
	close()
