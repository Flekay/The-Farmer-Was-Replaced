def swap_black():
    operations[0] = shuffle_black

def shuffle_black():
    operations[0] = swap_black2

def swap_black2():
    operations[0] = harvest_black

def harvest_black():
    operations[0] = swap_black

operations = [swap_black]



start = get_op_count()

operations[measure()]()

quick_print((get_op_count()-start-4))