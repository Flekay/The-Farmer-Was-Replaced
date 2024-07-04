def generate_finish(state, dino):
    forward = directions[dino]
    right = directions[(dino+1)%4]
    back = directions[(dino+2)%4]
    left = directions[(dino+3)%4]
    
    def stage1_finish():
        swap(forward)
        use_item(Egg)
        current[0] = starters[state][measure()]
    def stage2_finish():
        move(forward)
        swap(forward)
        swap(back)
        swap(right)
        move(back)
        use_item(Egg)
        current[0] = starters[state][measure()]
    def stage3_finish():
        swap(forward)
        use_item(Egg)
        current[0] = starters[state][measure()]
    def stage4_finish():
        harvest()
        use_item(Egg)
        current[0] = starters[state][measure()]
    
    res_func = [stage1_finish,stage2_finish,stage3_finish,stage4_finish][state[dino]]
    state[dino] += 1
    state[dino] %= 4
    [dir1,dir2,dir3,dir4] = state
    state = (dir1,dir2,dir3,dir4)
    return res_func


def generate_main(next_layer, state, dino):
    forward = directions[dino]
    right = directions[(dino+1)%4]
    back = directions[(dino+2)%4]
    left = directions[(dino+3)%4]
    
    def stage1_main():
        swap(forward)
        use_item(Egg)
        next[measure()]()
    def stage2_main():
        move(forward)
        swap(forward)
        swap(back)
        swap(right)
        move(back)
        use_item(Egg)
        next[measure()]()
    def stage3_main():
        swap(forward)
        use_item(Egg)
        next[measure()]()
    def stage4_main():
        harvest()
        use_item(Egg)
        next[measure()]()
    
    res_func = [stage1_main,stage2_main,stage3_main,stage4_main][state[dino]]
    state[dino] += 1
    state[dino] %= 4
    [dir1,dir2,dir3,dir4] = state
    state = (dir1,dir2,dir3,dir4)
    next = next_layer[state]
    return res_func



Egg = Items.Egg
go_to = generate_go_to()
directions = [North, East, South, West]


DEPTH = 300


starters = {}
for dir1 in range(4):
    for dir2 in range(4):
        for dir3 in range(4):
            for dir4 in range(4):
                functions = []
                for dino in range(4):
                    functions.append(generate_finish([dir1,dir2,dir3,dir4], dino))
                starters[dir1,dir2,dir3,dir4] = functions

for i in range(DEPTH):
    new_starters = {}
    for dir1 in range(4):
        for dir2 in range(4):
            for dir3 in range(4):
                for dir4 in range(4):
                    functions = []
                    for dino in range(4):
                        functions.append(generate_main(starters, [dir1,dir2,dir3,dir4], dino))
                    new_starters[dir1,dir2,dir3,dir4] = functions
    starters = new_starters

clear()

for i in range(10):
    for j in range(10):
        till()
        while measure() != 0:
            harvest()
            use_item(Items.Egg)
        smart_move()
go_to(5,5)

harvest()
use_item(Egg)
current = [starters[0,0,0,0][measure()]]
for i in range(0,1,0):
    current[0]()

current = [None]