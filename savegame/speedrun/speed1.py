def speed1():
    for i in range(13):
        harvest()
        plant(Entities.Bush)
        move(North)
    unlock(Unlocks.Speed)