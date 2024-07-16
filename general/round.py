def round(number, decimals=0):
	multiplier = 10 ** decimals
	if number >= 0:
		return (number * multiplier + 0.5) // 1 / multiplier
	else:
		return (number * multiplier - 0.5) // 1 / multiplier
