# ---------------------------------- PROBLEM 2 (HARD) --------------------------------------#
# Subarray Sort

# Write a function that takes in an array of integers of length at least 2. The function should 
# return an array of the starting and ending indices of the smallest subarray in the input array 
# that needs to be sorted in place in order for the entire input array to be sorted. If the input 
# array is already sorted, the function should return [-1, -1].

# Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# Sample output: [3, 9]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1) 
def subarraySort(lst):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	# iterate all numbers
	for idx in range(len(lst)):
		# number under consideration
		num = lst[idx]
		if isOutOfOrder(idx, num, lst):
			# update min and max numbers
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)

	# if the list is already sorted 
	if minOutOfOrder == float("inf"):
		return [-1, -1]

	# Find the position of minOutOfOrder
	subarrayLeftIdx = 0
	while minOutOfOrder >= lst[subarrayLeftIdx]:
		subarrayLeftIdx += 1

	# Find the position of maxOutOfOrder
	subarrayRightIdx = len(lst) - 1
	while maxOutOfOrder <= lst[subarrayRightIdx]:
		subarrayRightIdx -= 1

	return [subarrayLeftIdx, subarrayRightIdx]	

	
def isOutOfOrder(i, num, lst):
	if i == 0:
		return num > lst[i + 1]
	if i == len(lst)-1:
		return num < lst[i - 1]
	return num > lst[i + 1] or num < lst[i - 1]
# ----------------METHOD 01---------------------#