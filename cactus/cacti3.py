clear()
till()
move(North)
till()
move(East)
move(South)
till()
move(West)




CACTUS = Entities.Cactus

for i in range(0,1,0):
	plant(CACTUS)
	swap(North)
	plant(CACTUS)
	swap(East)
	plant(CACTUS)
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
	harvest()