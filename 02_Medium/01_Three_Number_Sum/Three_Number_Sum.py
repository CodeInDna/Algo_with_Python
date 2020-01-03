# ---------------------------------- PROBLEM 1 (MEDIUM) --------------------------------------#
# Three Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer 
# representing a target sum. The function should find all triplets in the array that sum up to 
# the target sum and return a two-dimensional array of all these triplets. The numbers in each 
# triplet should be ordered in ascending order, and the triplets themselves should be ordered 
# in ascending order with respect to the numbers they hold. If no three numbers sum up to the 
# target sum, the function should return an empty array.

# Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
# Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(n) 
def threeNumberSum(lst, target):
	lst.sort()
	triplets = []
	for i in range(len(lst)-2):
		left = i + 1
		right = len(lst) - 1
		while left < right:
			currSum = lst[i] + lst[left] + lst[right]
			if currSum == target:
				triplets.append([lst[i], lst[left], lst[right]])
				left += 1
				right -= 1
			elif currSum > target:
				right -= 1
			elif currSum < target:
				left += 1
	return triplets 
# ----------------METHOD 01---------------------#
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))