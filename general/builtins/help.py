# Prints a help message for a module.
#
# Arguments:
#	module (module): the module to print help for
#
# Example:
#	import math
#	help(math)
def help(module):
	quick_print(module.__name__, "Help")
	quick_print("functions:")
	quick_print(module.functions)
	quick_print("")
	quick_print("constants:")
	quick_print(module.constants)
	return ""
