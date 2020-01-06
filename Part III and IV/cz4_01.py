#!/usr/bin/python3

from board_driver_simulator import open, close, set_port, get_port
import time 

'''
1. Napisać program który będzie cyklicznie przesuwał
punkt świetlny (0,1,2,3,0,1,...) co ok. ¼ sekundy
'''

try: 
    open()  
#---------------------     
    while(True):     
       set_port(1<<13)
       time.sleep(0.25)
       set_port(1<<5)
       time.sleep(0.25)
       set_port(1<<9)
       time.sleep(0.25)
       set_port(1<<17)
       time.sleep(0.25)
#--------------------- 
finally: 
    close()
    