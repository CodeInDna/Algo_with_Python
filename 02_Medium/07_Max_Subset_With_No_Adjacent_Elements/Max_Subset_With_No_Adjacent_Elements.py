# ---------------------------------- PROBLEM 7 (MEDIUM) --------------------------------------#
# Maximum Subset Sum With No Adjacent Elements
# Write a function that takes in an array of positive integers and returns an integer representing 
# the maximum sum of non-adjacent elements in the array. If a sum cannot be generated, the function 
# should return 0.

# Sample input: [75, 105, 120, 75, 90, 135]
# Sample output: 330 (75, 120, 135)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def maxSubsetSumNoAdjacent(lst):
	if not len(lst):
		return 0
	if len(lst) == 1:
		return lst[0]
	# Generate empty list of length n i.e. similar to the length of given list of numbers
	maxSum = [None] * len(lst)
	# set the first two numbers
	maxSum[0] = lst[0]
	maxSum[1] = max(lst[0], lst[1])
	for i in range(2, len(lst)):
		maxSum[i] = max(maxSum[i-1], maxSum[i-2] + lst[i])
	return maxSum[-1]

# Working:
# Given: [7,10,12,7,9,14]
	# * Create a list of length equal to the given lst here maxSum = [None, None, None, None, None, None]
	# * Set the first element to be the first number given in the list i.e 1, maxSum = [7, None, None, None, None, None]
	# * Compare 1st and 2nd number of the list i.e max(7, 10) is 10, maxSum = [7, 10, None, None, None, None]
	# * Now compare the (i-1)th element of maxSum to the sum of (i-2)th element of maxSum and ith element of list
	# * ex: let's say i=2, compare max(maxSum[1], maxSum[0]+lst[2]) => max(10, 19) => 19, 19 becomes the 3rd element of maxSum and So on
	# * This question is solved by DYNAMIC PROGRAMMING
# ----------------METHOD 01---------------------#
print(maxSubsetSumNoAdjacent([7,10,12,7,9,14]))
