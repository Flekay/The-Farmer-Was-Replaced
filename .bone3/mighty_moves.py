clear()
lr_now = West
lr_other = East
r9 = range(9)
for udr in (North, South):
	for i in r9:
		logic(udr)
		temp = lr_now
		lr_now = lr_other
		lr_other = temp
		logicx4(lr_now)
	logicx4(lr_now)
	logic(lr_now)
quick_print(get_tick_count()-40000-200)

def logic(dir):
	move(dir)
	till()

def logicx4(dir):
	logic(dir)
	logic(dir)
	logic(dir)
	logic(dir)




clear()
lr_now = West
lr_other = East
r4 = range(4)
r5 = range(5)
r9 = range(9)
for udr in (North, South):
	for i in r9:
		move(udr)
		till()
		temp = lr_now
		lr_now = lr_other
		lr_other = temp
		for _ in r4:
			move(lr_now)
			till()
	for _ in r5:
		move(lr_now)
		till()
quick_print(get_tick_count()-40000-200)
