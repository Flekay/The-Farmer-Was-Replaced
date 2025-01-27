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
