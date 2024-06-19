# 60s stats 16.6k
def farmBoneHard(count=2000):
    setupBones()
    
    # Dinosaur counts
    dino_black = 0
    dino_brown = 0
    dino_white = 0
    dino_grey = 0
    
    # Items
    egg = Items.Egg
    
    while 1:
        use_item(egg)
        colour = measure()
        
        if colour == 0:
            dino_black += 1
            if dino_black == 1:
                swap(North)
            elif dino_black == 2:
                move(North)
                swap(North)
                move(South)
                swap(North)
            elif dino_black == 3:
                move(North)
                swap(East)
                move(South)
                swap(North)
            else:
                harvest()
                dino_black = 0
        
        elif colour == 1:
            dino_brown += 1
            if dino_brown == 1:
                swap(East)
            elif dino_brown == 2:
                move(East)
                swap(East)
                move(West)
                swap(East)
            elif dino_brown == 3:
                move(East)
                swap(South)
                move(West)
                swap(East)
            else:
                harvest()
                dino_brown = 0
        
        elif colour == 2:
            dino_white += 1
            if dino_white == 1:
                swap(South)
            elif dino_white == 2:
                move(South)
                swap(South)
                move(North)
                swap(South)
            elif dino_white == 3:
                move(South)
                swap(West)
                move(North)
                swap(South)
            else:
                harvest()
                dino_white = 0
        
        elif colour == 3:
            dino_grey += 1
            if dino_grey == 1:
                swap(West)
            elif dino_grey == 2:
                move(West)
                swap(West)
                move(East)
                swap(West)
            elif dino_grey == 3:
                move(West)
                swap(North)
                move(East)
                swap(West)
            else:
                harvest()
                dino_grey = 0
farmBoneHard()