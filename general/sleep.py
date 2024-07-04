def sleep(seconds):
	start = get_time()
	scale = 1/((num_unlocked(Unlocks.Speed)+1)*16)
	if num_unlocked(Unlocks.Sunflowers) > 0:
		scale = 1/((num_unlocked(Unlocks.Speed)+1)*16*2)
	while get_time() - start < seconds - seconds * scale/seconds:
		pass