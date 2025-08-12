help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/random"
constants   = "[]"
functions   = "[choice, choices, randint, sample, shuffle]"

# Chooses a random element from a list.
#
# Arguments:
#	mylist (list): the list to choose from
#
# Returns:
#	any: a random element from the list
#
# Example:
#	choice([1, 2, 3])
#	# 2
def choice(mylist):
	return mylist[random() * len(mylist)]

# Chooses a random element from a list. If weights are provided, the probability of each element being chosen is proportional to its weight.
#
# Arguments:
#	population (list): the list to choose from
#	weights (list): the weights for each element in the population (default is None)
#	k (int): the number of elements to choose (default is 1)
#
# Returns:
#	list: a list of random elements from the population
#
# Example 1:
#	choices([1, 2, 3], [1, 2, 1], 2)
#	# [2, 1]
def choices(population, weights=None, k=1):
	if weights == None:
		weights = []
	_weights = []
	for i in range(len(population)):
		if i < len(weights):
			_weights.append(weights[i])
		else:
			_weights.append(1)

	# Calculate cumulative weights
	cum_weights = []
	total = 0
	for w in _weights:
		total += w
		cum_weights.append(total)

	# Make selections using binary search
	result = []
	for _ in range(k):
		r = random() * total
		left = 0
		right = len(cum_weights)
		while left < right:
			mid = (left + right) // 2
			if cum_weights[mid] < r:
				left = mid + 1
			else:
				right = mid
		result.append(population[left])

	return result

# Returns a random integer between two given integers.
#
# Arguments:
#	low (int): the lower bound of the random integer
#	high (int): the upper bound of the random integer
#
# Returns:
#	int: a random integer between low and high
#
# Example 1:
#	randint(1, 10)
#	# 7
def randint(low, high):
	return (random() * (high - low + 1) + low) // 1

# Chooses a random sample of elements from a list.
#
# Arguments:
#	population (list): the list to choose from
#	k (int): the number of elements to choose
#
# Returns:
#	list: a list of random elements from the population
#
# Example 1:
#	sample([1, 2, 3], 2)
#	# [2, 1]
def sample(population, k):
	if k > len(population):
		k = len(population)

	result = list(population)
	for i in range(len(result) - 1, len(result) - k - 1, -1):
		j = random() * (i + 1)
		result[i], result[j] = result[j], result[i]
	return result[-k:]

# Shuffles a list in place.
#
# Arguments:
#	lst (list): the list to shuffle
#
# Returns:
#	list: the shuffled list
#
# Example:
#	shuffle([1, 2, 3])
#	# [2, 1, 3]
def shuffle(lst):
	for i in range(len(lst) - 1, 0, -1):
		j = random() * (i + 1)
		temp = lst[i]
		lst[i] = lst[j]
		lst[j] = temp
	return lst

