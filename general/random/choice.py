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
