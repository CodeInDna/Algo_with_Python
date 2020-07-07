# ---------------------- PROBLEM 26 (RANDOM) ----------------------------------#
# Write a function called capitalizeWords. Given an array of strings, 
# capitalize the each word of each string in the array.

# Sample input: ['car', 'taco', 'banana']
# Sample output: ['CAR', 'TACO', 'BANANA']

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def capitalizeWords(arr):
	if len(arr) == 0: return arr

	return [arr[0].upper()] + capitalizeWords(arr[1:])
# ----------------METHOD 01---------------------#