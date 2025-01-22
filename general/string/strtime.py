def strtime(seconds):
	# Flotating point error correction
	seconds += 0.00000000001

	# Format minutes
	if seconds >= 6000:
		min_str = str(seconds // 60)
	elif seconds >= 600:
		min_str = ' ' + str(seconds // 60)
	else:
		min_str = '  ' + str(seconds // 60)

	# Format seconds
	sec_str = "0123456789"[seconds // 10 % 6] + "0123456789"[seconds % 10]

	# Format fraction (2 digits)
	frac_str = "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]

	# Format fraction (4 digits)
	# frac_str = "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10] + "0123456789"[seconds * 1000 % 10] + "0123456789"[seconds * 10000 % 10]

	# Construct the result string
	return min_str + ":" + sec_str + "." + frac_str
