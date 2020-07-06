# ---------------------- PROBLEM 23 (RANDOM) ----------------------------------#
# Write a function called flatten which accepts an array of arrays and returns 
# a new arrays and returns a new array with all values flattened.

# Sample input: [1, 2, 3, [4, 5]]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def flatten(arr):
	if len(arr) == 0: return arr

	if type(arr[0]) == list:
		return flatten(arr[0]) + flatten(arr[1:])

	return arr[:1] + flatten(arr[1:])
# ----------------METHOD 01---------------------#
