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
	
def steps(direction, nsteps):
	global vstep
	if direction=='right':
		vstep+=1
	elif direction=='left':
		vstep-=1
	vstep%=4
	for i in range(nsteps):
		led(set_point(vstep))
		step(direction)
		
def step_by_key(key):
	if key==0:
		steps('left', 12)
	elif key==1:
		steps('left', 3)
	elif key==2:
		steps('right', 3)
	elif key==3:
		steps('right', 12)

def get_detector():
	if det():
		return 'active'
	return 'no_active'
	
def wait_for_key():
	while True:
		key_state=get_key()
		if(key_state!=-1):
			return key_state
