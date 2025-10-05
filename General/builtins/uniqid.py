_id_counter = 0
# Generates a unique identifier.
#
# Returns:
#	int: a unique identifier
#
# Example:
#	uniqid()
#	# 1
def uniqid():
	global _id_counter
	_id_counter += 1
	return _id_counter
