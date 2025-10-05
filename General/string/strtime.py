# Converts a number of seconds to a string in the format 'mm:ss.ff'.
#
# Arguments:
#	seconds (float): the number of seconds
#
# Returns:
#	str: the time string
#
# Example 1:
#	strtime(123.45)
#	# ' 2:03.45'
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
