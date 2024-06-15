#plant(Entities.Bush)
harvest()
start = get_time()
while not can_harvest():
    pass
quick_print("Bush grows in:", str(get_time() - start), "seconds")