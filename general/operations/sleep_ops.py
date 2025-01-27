# Sleeps for a specified number of ticks. (minimum of 3)
#
# Arguments:
#	ops (int): the number of ticks to sleep for (default is 3)
#
# Example 1:
#	sleep_ops(5)
def sleep_ops(ops=3):
	list(range(ops-3))
