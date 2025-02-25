# Returns the number of ticks per second based on the number of speed unlocks and whether the power item is owned.
#
# Arguments:
#	speed_unlocks (int): the number of speed unlocks (default is `num_unlocked(Unlocks.Speed)`)
#	power (bool): whether the power item is owned (default is `num_items(Items.Power) > 0`)
#
# Returns:
#	number: the number of ticks per second
#
# Example:
#	ops()
#	# 16800
def ops(speed_unlocks=(num_unlocked(Unlocks.Speed)), power=(num_items(Items.Power) > 0)):
	return 400 * (speed_unlocks + 1) * (power + 1)
