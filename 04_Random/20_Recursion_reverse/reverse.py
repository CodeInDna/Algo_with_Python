# ---------------------- PROBLEM 20 (RANDOM) ----------------------------------#
# Write a function called reverse which accpets a string and returns a new string in reverse.

# Sample input: 'awesome'
# Sample output: 'emosewa'

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def reverse(string):

	if len(string) == 0:
		return ''

	return string[-1] + reverse(string[:-1])
# ----------------METHOD 01---------------------#
