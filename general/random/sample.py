def sample(population, k):
	if k > len(population):
		k = len(population)

	result = list(population)
	for i in range(len(result) - 1, len(result) - k - 1, -1):
		j = random() * (i + 1)
		result[i], result[j] = result[j], result[i]
	return result[-k:]
