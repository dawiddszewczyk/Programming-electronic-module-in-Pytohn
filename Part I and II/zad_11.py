#!/usr/bin/python3

'''
11. Program z poprzedniego punktu stosunkowo wolno reaguje na
przyciski. Przyczyną jest stosunkowo długi czas wykonania funkcji
but(). Zmodyfikować program tak aby wywoływał funkcję but() tylko
raz na jeden obrót pętli. Jak modyfikacja skróciła reakcji 
programu na naciśnięcie przycisku?
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		but_state=but()
		if but_state==1:
			led(0x8)
		elif but_state==2:
			led(0xC)
		elif but_state==4:
			led(0xE)
		elif but_state==8:
			led(0xF)
		else:
			led(0x0)
#---------------------
finally:
	close()
