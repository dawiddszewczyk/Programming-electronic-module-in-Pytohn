#!/usr/bin/python3

from my_board import *
import time

'''
5.
Wstawić zdefiniowane funkcje do modułu „my_board”. 
Test: Test z zad. 4. 
Test:  Program  obracający  tarczą  po  każdym  naciśnięciu
przycisku.  Kierunek  obrotu  i  liczba  kroków  zależna 
od naciśniętego przycisku w sposób nast.: 
0:left,12 
1:left,3 
2:right,3 
3:right,12 
'''

try:
	open()
#---------------------
	while(True):
		step_by_key(wait_for_key()); time.sleep(0.5) 
#---------------------
finally:
	close()
