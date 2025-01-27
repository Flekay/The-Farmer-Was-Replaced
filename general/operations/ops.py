# Returns the current number of ticks per second.
#
# Returns:
#	number: the number of ticks per second
#
# Example:
#	ops()
#	# 16800
def ops():
	return 400 * (1 + num_unlocked(Unlocks.Speed)) * (1 + (num_items(Items.Power) > 0))
