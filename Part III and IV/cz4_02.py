#!/usr/bin/python3

from board_driver_simulator import open, close, set_port, get_port
import time 

'''
2. Zmodyfikować funkcję set_point tak aby korzystała z
portu wYjściowego. Użyć przesunięcia bitowego. 
Test:  Funkcjonalność z poprzedniego zadania
(cyklicznie przesuwał punkt świetlny (0,1,2,3,0,1,...)
co ok. ¼ sekundy) 
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

try: 
    open()  
#---------------------     
    while(True):     
       set_point(0)
       time.sleep(0.25)
       set_point(1)
       time.sleep(0.25)
       set_point(2)
       time.sleep(0.25)
       set_point(3)
       time.sleep(0.25)
#--------------------- 
finally: 
    close()
