def sleep(secs = 1):
    start = get_time()
    scale = 1/((num_unlocked(Unlocks.Speed)+1)*16)
    if num_unlocked(Unlocks.Sunflowers) > 0:
        scale = 1/((num_unlocked(Unlocks.Speed)+1)*16*2)
    while get_time() - start < secs - secs * scale/secs:
        pass
start = get_time()
sleep(1)
quick_print(str(get_time() - start))