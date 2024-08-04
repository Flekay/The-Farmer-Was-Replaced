def str(number, precision = 4):
	negative = False
	precision = abs(precision)
	if number <= 0:
		if number == 0:
			return "0"
		number = abs(number)
		negative = True
	string = ""
	n = "0123456789"
	number = (number * (10**precision) + 0.5)
	number //= 1
	for i in range(precision):
		string = n[number %10] + string
		number //= 10
	if precision != 0:
		string = "."+string
	while number > 0:
		string = n[number% 10] + string
		number //= 10
	if string[0] != ".":
		if negative:
			return "-" + string
		return string
	if negative:
			return "-0" + string
	return  "0" + string
	