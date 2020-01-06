#!/usr/bin/python3

'''
10. Program zapalający pasek diod. Długość paska zależna od
naciśnietego przycisku (But0->1000, But1- >1100, But2- >1110,
But3->1111). Jeżeli nie będzie naciśnięty żaden przycisk wszystkie
diody powinny być zgaszone. Użyć zapisu heksadecymalnego. 
W instrukcji warunkowej użyć wywołania funkcji but() (5 razy)
'''

from board_driver_simulator import open,close,but,pot,det,led

try:
	open()
#---------------------
	while(True):
		if but()==1:
			led(0x8)
		elif but()==2:
			led(0xC)
		elif but()==4:
			led(0xE)
		elif but()==8:
			led(0xF)
		else:
			led(0x0)
#---------------------
finally:
	close()
