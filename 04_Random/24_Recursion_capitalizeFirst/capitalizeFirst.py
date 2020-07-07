# ---------------------- PROBLEM 24 (RANDOM) ----------------------------------#
# Write a function called capitalizeFirst. Given an array of strings, 
# capitalize the first letter of each string in the array.

# Sample input: ['car', 'taco', 'banana']
# Sample output: ['Car', 'Taco', 'Banana']

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def capitalizeFirst(arr):
	if len(arr) == 0: return arr

	return [arr[0].capitalize()] + capitalizeFirst(arr[1:])
# ----------------METHOD 01---------------------#
