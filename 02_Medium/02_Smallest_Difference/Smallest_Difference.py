# ---------------------------------- PROBLEM 2 (MEDIUM) --------------------------------------#
# Smallest Difference
# Write a function that takes in two non-empty arrays of integers. The function should find the 
# pair of numbers (one from the first array, one from the second array) whose absolute difference 
# is closest to zero. The function should return an array containing these two numbers, with the 
# number from the first array in the first position. Assume that there will only be one pair of 
# numbers with the smallest difference.

# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
# Sample output: [28, 26]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
def smallestDifference(lst1, lst2):
	smallDiff = float("inf")
	firstNum = None
	secNum = None
	for num1 in lst1:
		for num2 in lst2:
			currDiff = abs(num1 - num2)
			if currDiff < smallDiff:
				smallDiff = currDiff
				firstNum = num1
				secNum = num2
	return [firstNum, secNum] 
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(nlog(n) + mlog(m)), where n,m = length of lst1, lst2, SPACE: O(1) 
def smallestDifference(lst1, lst2):
	lst1.sort()
	lst2.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	currDiff = float("inf")
	smallestPair = []
	while idxOne < len(lst1) and idxTwo < len(lst2):
		firstNum = lst1[idxOne]
		secNum = lst2[idxTwo]
		if firstNum < secNum:
			currDiff = secNum - firstNum
			idxOne += 1
		elif secNum < firstNum:
			currDiff = firstNum - secNum
			idxTwo += 1
		else:
			return [firstNum, secNum]
		if smallest > currDiff:
			smallest = currDiff
			smallestPair = [firstNum, secNum]
	return smallestPair
# ----------------METHOD 02---------------------#
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))