
def x2y2(mov=move, extend=False):
	if extend or not mov(North):
		mov(West)
		if measure(North):
			mov(North)
			mov(East)
		else:
			mov(West)
			mov(North)
			mov(East)
			mov(East)
	return x2y3

def x2y3(mov=move, extend=False):
	mov(North)
	return x2y4

def x2y4(mov=move, extend=False):
	if extend or not mov(North):
		mov(West)
		if measure(North):
			mov(North)
			mov(East)
		else:
			mov(West)
			mov(North)
			mov(East)
			mov(East)
	return x2y5

def x2y5(mov=move, extend=False):
	if extend or not mov(North):
		mov(East)
		if measure(North):
			mov(North)
			mov(West)
		else:
			mov(East)
			mov(North)
			mov(West)
			mov(West)
	return x2y6

def x2y6(mov=move, extend=False):
	if extend or not mov(North):
		mov(West)
		mov(West)
		mov(North)
		if measure(East):
			mov(East)
			mov(East)
		else:
			mov(North)
			if measure(East):
				mov(East)
				mov(South)
				mov(East)
			else:
				mov(North)
				mov(East)
				mov(South)
				mov(South)
				mov(East)
	return x2y7

def x2y7(mov=move, extend=False):
	if extend or not mov(East):
		mov(North)
		if measure(East):
			mov(East)
			mov(South)
		else:
			mov(North)
			mov(East)
			mov(South)
			mov(South)
	return x3y7

def x3y7(mov=move, extend=False):
	mov(East)
	return x4y7

def x4y7(mov=move, extend=False):
	if extend or not mov(East):
		mov(North)
		if measure(East):
			mov(East)
			mov(South)
		else:
			mov(North)
			mov(East)
			mov(South)
			mov(South)
	return x5y7

def x5y7(mov=move, extend=False):
	if extend or not mov(East):
		mov(South)
		if measure(East):
			mov(East)
			mov(North)
		else:
			mov(South)
			mov(East)
			mov(North)
			mov(North)
	return x6y7

def x6y7(mov=move, extend=False):
	if extend or not mov(East):
		mov(North)
		mov(North)
		mov(East)
		if measure(South):
			mov(South)
			mov(South)
		else:
			mov(East)
			if measure(South):
				mov(South)
				mov(West)
				mov(South)
			else:
				mov(East)
				mov(South)
				mov(West)
				mov(West)
				mov(South)
	return x7y7

def x7y7(mov=move, extend=False):
	if extend or not mov(South):
		mov(East)
		if measure(South):
			mov(South)
			mov(West)
		else:
			mov(East)
			mov(South)
			mov(West)
			mov(West)
	return x7y6

def x7y6(mov=move, extend=False):
	mov(South)
	return x7y5

def x7y5(mov=move, extend=False):
	if extend or not mov(South):
		mov(East)
		if measure(South):
			mov(South)
			mov(West)
		else:
			mov(East)
			mov(South)
			mov(West)
			mov(West)
	return x7y4

def x7y4(mov=move, extend=False):
	if extend or not mov(South):
		mov(West)
		if measure(South):
			mov(South)
			mov(East)
		else:
			mov(West)
			mov(South)
			mov(East)
			mov(East)
	return x7y3

def x7y3(mov=move, extend=False):
	if extend or not mov(South):
		mov(East)
		mov(East)
		mov(South)
		if measure(West):
			mov(West)
			mov(West)
		else:
			mov(South)
			if measure(West):
				mov(West)
				mov(North)
				mov(West)
			else:
				mov(South)
				mov(West)
				mov(North)
				mov(North)
				mov(West)
	return x7y2

def x7y2(mov=move, extend=False):
	if extend or not mov(West):
		mov(South)
		if measure(West):
			mov(West)
			mov(North)
		else:
			mov(South)
			mov(West)
			mov(North)
			mov(North)
	return x6y2

def x6y2(mov=move, extend=False):
	mov(West)
	return x5y2

def x5y2(mov=move, extend=False):
	if extend or not mov(West):
		mov(South)
		if measure(West):
			mov(West)
			mov(North)
		else:
			mov(South)
			mov(West)
			mov(North)
			mov(North)
	return x4y2

def x4y2(mov=move, extend=False):
	if extend or not mov(West):
		mov(North)
		if measure(West):
			mov(West)
			mov(South)
		else:
			mov(North)
			mov(West)
			mov(South)
			mov(South)
	return x3y2

def x3y2(mov=move, extend=False):
	if extend or not mov(West):
		mov(South)
		mov(South)
		mov(West)
		if measure(North):
			mov(North)
			mov(North)
		else:
			mov(West)
			if measure(North):
				mov(North)
				mov(East)
				mov(North)
			else:
				mov(West)
				mov(North)
				mov(East)
				mov(East)
				mov(North)
	return x2y2
	