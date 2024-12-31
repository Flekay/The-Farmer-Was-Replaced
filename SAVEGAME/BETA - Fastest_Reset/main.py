unlock_cost = get_cost_list()
available_resources = get_available_resources_list()
farming_functions = get_farming_functions_list()

while num_unlocked(Unlocks.Carrots) < 1:
	unlockment, items = get_random_unlock()
	for item in items:
		quick_print("try to farm: ",items[item],item, "for", unlockment)
		farming_functions[item](items[item])
	if unlock(unlockment):
		#pass
		update_available_resources(unlockment)
	else:
		[] = [[],[]]