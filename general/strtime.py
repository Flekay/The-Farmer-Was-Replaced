def strtime(seconds):
	# Format minutes
	if seconds >= 6000:
		min_str = "0123456789"[seconds // 6000] + "0123456789"[(seconds % 6000) // 600] + "0123456789"[(seconds % 600) // 60]
	elif seconds >= 600:
		min_str = ' ' + "0123456789"[seconds // 600] + "0123456789"[(seconds % 600) // 60]
	else:
		min_str = '  ' + "0123456789"[seconds // 60]

	# Format seconds
	sec_str = "0123456789"[seconds * 0.1 % 10] + "0123456789"[seconds % 10]

	# Format fraction
	frac_str = "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]

	# Construct the result string
	return min_str + ":" + sec_str + "." + frac_str
