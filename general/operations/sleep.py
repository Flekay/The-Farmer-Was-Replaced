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
