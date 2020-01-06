#!/usr/bin/python3

'''
5. Funkcja get_detector() zwracająca ‘active’, jeżeli marker na tarczy
będzie znajdował się nad detektorem krańcowym oraz ‘no_active’ w 
przeciwnym przypadku.
Test 1: Program obracający tarczę w prawo i jednocześnie wyświetlający
wynik wywołania funkcji get_detector()
Test 2: Program, który będzie obracał tarczę w prawo do momentu aż marker
osiągnie detektor. Następnie program powinien kończyć działanie.
UWAGA: w celu ręcznego obrotu tarcz należy rozpiąć zworkę na czas obrotu.
'''

from board_driver_simulator import open,close,but,pot,det,led

vstep=0

def get_key():
	but_state=but()
	if but_state==1:
		return 0
	elif but_state==2:
		return 1
	elif but_state==4:
		return 2
	elif but_state==8:
		return 3
	else:
		return -1

def set_point(position):
	if position==0:
		return 1
	elif position==1:
		return 2
	elif position==2:
		return 4
	elif position==3:
		return 8
	else:
		return 0

def step(direction):
	global vstep
	if direction=='right':
		vstep+=1
	elif direction=='left':
		vstep-=1
	vstep%=4
	led(set_point(vstep))

def get_detector():
	if det():
		return 'active'
	return 'no_active'

try:
	open()
#---------------------
	led(0)
	while(True):
		#test1
		#step('right')
		#print(get_detector())	

		#test2
		step('right')
		if get_detector()=='active':
			exit()
#---------------------
finally:
	close()
