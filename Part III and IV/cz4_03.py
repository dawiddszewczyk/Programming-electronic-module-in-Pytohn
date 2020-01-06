#!/usr/bin/python3

from board_driver_simulator import open, close, set_port, get_port
import time 

'''
3.
Poniżej  pokazano  fragment  kodu  wyświetlający  stan  portu
wejściowego  w  kodzie  binarnym.  Wstawić  kod  do programu.
Przy użyciu programu zweryfikować przyporządkowanie peryferiów
do bitów portu wejściowego (rysunek we wprowadzeniu).
while(True)
	port_state=get_port()
	print(f"{port_state:032b}") # wyświetla wszystkie 32 bity zmiennej port_state  
'''

try: 
	open()  
#---------------------     
	while(True):     
		port_state=get_port()
		print(f"{port_state:032b}")
#--------------------- 
finally: 
    close()
    