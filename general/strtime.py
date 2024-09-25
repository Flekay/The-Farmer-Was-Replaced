def strtime(seconds):
	digits = "0123456789"

	# Format minutes
	if seconds >= 6000:
		min_str = digits[seconds // 6000] + digits[(seconds % 6000) // 600] + digits[(seconds % 600) // 60]
	elif seconds >= 600:
		min_str = ' ' + digits[seconds // 600] + digits[(seconds % 600) // 60]
	else:
		min_str = '  ' + digits[seconds // 60]

	# Format seconds
	sec_str = digits[seconds * 0.1 % 10] + digits[seconds % 10]

	# Format fraction
	frac_str = digits[seconds * 10 % 10] + digits[seconds * 100 % 10]

	# Construct the result string
	return min_str + ":" + sec_str + "." + frac_str


# minified version of strtime
def strtime(seconds):
    if seconds >= 6000:
        return "0123456789"[seconds // 6000] + "0123456789"[(seconds % 6000) // 600] + "0123456789"[(seconds % 600) // 60] + ":" + "0123456789"[seconds * 0.1 % 10] + "0123456789"[seconds % 10] + "." + "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]
    elif seconds >= 600:
        return ' ' + "0123456789"[seconds // 600] + "0123456789"[(seconds % 600) // 60] + ":" + "0123456789"[seconds * 0.1 % 10] + "0123456789"[seconds % 10] + "." + "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]
    else:
        return '  ' + "0123456789"[seconds // 60] + ":" + "0123456789"[seconds * 0.1 % 10] + "0123456789"[seconds % 10] + "." + "0123456789"[seconds * 10 % 10] + "0123456789"[seconds * 100 % 10]
