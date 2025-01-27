help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/operations"
constants   = "[]"
functions   = "[ops, sleep_ops, sleep]"

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

# Sleeps for a specified number of seconds.
#
# Arguments:
#	seconds (number): the number of seconds to sleep for
#
# Example 1:
#	sleep(5)
def sleep(seconds):
	correction = 13
	while seconds > 1:
		do_a_flip()
		seconds -= 1
		correction += 2
	for _ in range(seconds * 400 * (1 + num_unlocked(Unlocks.Speed)) * (1 + (num_items(Items.Power) > 0)) - correction):
		pass

# Sleeps for a specified number of ticks. (minimum of 3)
#
# Arguments:
#	ops (int): the number of ticks to sleep for (default is 3)
#
# Example 1:
#	sleep_ops(5)
def sleep_ops(ops=3):
	list(range(ops-3))

