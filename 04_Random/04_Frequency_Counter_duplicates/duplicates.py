# ---------------------- PROBLEM 03 (RANDOM) ----------------------------------#
# Implement a function called areThereDuplicates which accepts a variable number of
# arguments, and check whether there are any duplicates among the arguments passed in.

# Sample input: 1, 2, 2
# Sample output: False

# Sample input: 'a','b','c','a'
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
from collections import Counter
def areThereDuplicates(*args):
	for val in Counter(args).values():
		if val > 1:
			return True
	return False
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(1), SPACE: O(1)
def areThereDuplicates(*args):
	return len(set(args)) != len(args)
# ----------------METHOD 02---------------------#