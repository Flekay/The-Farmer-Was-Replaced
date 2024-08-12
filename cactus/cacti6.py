CACTUS = Entities.Cactus
cactus_setup()
move(East)
for i in range(0,1,0):
    cacti6()

def cactus_setup():
	clear()
	till()
	move(North)
	till()
	move(North)
	till()
	move(South)
	move(East)
	till()
	move(South)
	till()
	move(East)
	till()
	move(West)
	move(West)

def cacti6():
    plant(CACTUS)
    swap(East)
    plant(CACTUS)
    swap(North)
    plant(CACTUS)

    #If right < up
    if measure(East) < measure(North):
        if measure() > measure(East):
            swap(East)
    elif measure() > measure(North):
        swap(North)

    #Put current into a buffer
    swap(West)
    plant(CACTUS)
    if measure() < measure(West):
        swap(West)
    elif measure(East) > measure(North):
        if measure() > measure(North):
            swap(North)
    elif measure(North) >= measure(East):
        if measure() > measure(East):
            swap(East)

    move(North)
    move(West)

    plant(CACTUS)
    if measure() < measure(South):
        swap(South)
    swap(North)
    plant(CACTUS)
    if measure() < measure(South):
        swap(South)
    elif measure() > measure(East):
        swap(East)
    if measure() > measure(North):
        swap(North)

    harvest()

    plant(CACTUS)
    swap(North)
    plant(CACTUS)
    swap(East)
    plant(CACTUS)


    #If right < up
    if measure(North) < measure(East):
        if measure() > measure(North):
            swap(North)
    elif measure() > measure(East):
        swap(East)

    #Put current into a buffer
    swap(South)
    plant(CACTUS)
    if measure() < measure(South):
        swap(South)
    elif measure(North) > measure(East):
        if measure() > measure(East):
            swap(East)
    if measure(East) >= measure(North):
        if measure() > measure(North):
            swap(North)

    move(South)
    move(East)

    plant(CACTUS)
    if measure() < measure(West):
        swap(West)
    swap(East)
    plant(CACTUS)
    if measure() < measure(West):
        swap(West)
    elif measure() > measure(North):
        swap(North)
    if measure() > measure(East):
        swap(East)

    harvest()
