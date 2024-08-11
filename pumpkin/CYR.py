clear()

n=100
def t(f):
	while n:
		n-=move(North)
		i=f(),n%10 or move(East)
def a():
	while not can_harvest():
		plant(Entities.Pumpkin)
		use_item(Items.Fertilizer)
t(till)
while 1:
	t(a)
	harvest()
