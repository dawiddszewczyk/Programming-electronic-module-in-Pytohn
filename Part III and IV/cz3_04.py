#!/usr/bin/python3

from my_board import *
import time

'''
4.
Zmodyfikować funkcję wait_for_key() tak aby dodatko
wo zwracała numer naciśnietego przycisku. 
Test:  Program  obracający  tarczą  po  każdym  naciśnięciu
przycisku.  Kierunek  obrotu  i  liczba  kroków  zależna od 
naciśniętego przycisku w sposób nast.: 
0:left,12 
1:left,3 
2:right,3 
3:right,12 
'''

try:
	open()
#---------------------
	while(True):
		key=wait_for_key()
		if key==0:
			steps('left', 12); time.sleep(0.5) 
		elif key==1:
			steps('left', 3); time.sleep(0.5) 
		elif key==2:
			steps('right', 3); time.sleep(0.5) 
		elif key==3:
			steps('right', 12); time.sleep(0.5) 
#---------------------
finally:
	close()
