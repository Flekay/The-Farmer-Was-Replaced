def string(number, precision = 4):
	if number >= 0:
		string = str(number//1)
	else:
		string = str(-(-number // 1))
	if precision > 0:
		string += "."
		number = abs(number)
		for _ in range(precision):
			number = (number * 10) % 10
			string += str(number//1)
	return string
