# ---------------------- PROBLEM 14 (RANDOM) ----------------------------------#
# Write a function called collectOddValues which takes in array of numbers and 
# return the odd values in an array using recursion

# Sample input: [1,2,3,4,5]
# Sample output: [1,3,5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def collectOddValues(arr, result=[]):
	if len(arr) == 0:
		return result

	if arr[0] % 2 != 0:
		result.append(arr[0])

	return collectOddValues(arr[1:], result)
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# Using Helper function
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def collectOddValues(arr):

	result = []

	def helper(arr):

		if len(arr) == 0:
			return result

		if arr[0] % 2 != 0:
			result.append(arr[0])

		helper(arr[1:])

	helper(arr)

	return result
# ----------------METHOD 02---------------------#