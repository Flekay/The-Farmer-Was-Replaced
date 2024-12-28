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
