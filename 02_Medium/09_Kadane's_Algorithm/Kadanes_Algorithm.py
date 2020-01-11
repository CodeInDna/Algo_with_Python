# ---------------------------------- PROBLEM 09 (MEDIUM) --------------------------------------#
# Kadane's Algorithm
# Write a function that takes in a non-empty array of integers and returns the maximum sum that can be 
# obtained by summing up all the numbers in a non-empty subarray of the input array. A subarray must 
# only contain adjacent numbers.

# Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
# Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1) 
def kadanesAlgorithm(lst):
	maxSoFar = lst[0]
	maxEndingHere = lst[0]
	for i in range(1, len(lst)):
		num = lst[i]
		maxEndingHere = max(maxEndingHere + num, num)
		maxSoFar = max(maxEndingHere, maxSoFar)
	return maxSoFar
# ----------------METHOD 01---------------------#
print(kadanesAlgorithm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
