#!/usr/bin/python3

from my_board import *
import time

'''
1.
Wstawić zdefiniowane funkcje do modułu „my_board”. 
Test 1: Cześć II, Zadanie 4, Test 1:
	4. Modyfikacja funkcji step pozwalająca na określenie kierunku 
	przesunięcia:
	step(‘right’) # 0->1
	step(‘right’) # 1->2
	step(‘left’) # 2->1
	step(‘left’) # 1->0
	Test 1: Program: obracający krążkiem w lewo jeżeli naciśnieto 
	przycisk ‘0’ a w prawo jeśli naciśnieto przycisk ‘1’
Test 2: Cześć II, Zadanie 5, Test 2
	5. Funkcja get_detector() zwracająca ‘active’, jeżeli marker na tarczy
	będzie znajdował się nad detektorem krańcowym oraz ‘no_active’ w 
	przeciwnym przypadku.
	Test 2: Program, który będzie obracał tarczę w prawo do momentu aż marker
	osiągnie detektor. Następnie program powinien kończyć działanie.
	UWAGA: w celu ręcznego obrotu tarcz należy rozpiąć zworkę na czas obrotu.
'''

try:
	open()
#---------------------
	while(True):
		#test1
		if get_key()==0:
			step('left')
		elif get_key()==1:
			step('right')
			
		#test2
		if get_detector()=='active':
			exit()
#---------------------
finally:
	close()
