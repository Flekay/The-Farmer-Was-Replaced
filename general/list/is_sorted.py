def is_sorted(list):
	for i in list:
		arm1 = i
		break
	for i in list:
		if i < arm1:
			return False
		arm1 = i
	return True
