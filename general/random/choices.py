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
