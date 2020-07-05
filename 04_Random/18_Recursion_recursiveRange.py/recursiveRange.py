# ---------------------- PROBLEM 18 (RANDOM) ----------------------------------#
# Write a function called recursiveRange which accepts a number and addes up all
# the numbers from 0 to the number passed to the function.

# Sample input: 6
# Sample output: 21

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def recursiveRange(num):
	if num == 1: return 1

	return num + recursiveRange(num-1)
# ----------------METHOD 01---------------------#