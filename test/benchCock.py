def swap_black():
    return shuffle_black

def shuffle_black():
    return swap_black2

def swap_black2():
    return harvest_black

def harvest_black():
    return swap_black

operations = [swap_black]

start = get_op_count()
color = measure()
operations[color] = operations[color]()

quick_print((get_op_count()-start-4))