# ---------------------------------- PROBLEM 06 (EASY) --------------------------------------#
# Binary Search
# Write a function that takes in a sorted array of integers as well as a target integer. The 
# function should use the Binary Search algorithm to find if the target number is contained in 
# the array and should return its index if it is, otherwise -1.

# Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
# Sample output: 3
import math
# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(logn), SPACE: O(1)
def binarySearch(lst, num):
	left = 0
	right = len(lst) - 1
	while left <= right:
		mid = (left + right) // 2
		if lst[mid] == num:
			return mid
		elif lst[mid] > num:
			right = mid - 1
		else:
			left = mid + 1
	return -1
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(), SPACE: O()
def binarySearch(lst, target):
	return binarySearchHelper(lst, target, 0, len(lst)-1)

def binarySearchHelper(lst, target, left, right):
	if left > right:
		return -1
	mid = (left + right) // 2
	potentialMatch = lst[mid]
	if potentialMatch == target:
		return mid
	elif potentialMatch > target:
		return binarySearchHelper(lst, target, left, mid - 1)
	else:
		return binarySearchHelper(lst, target, mid + 1, right)
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# ----------------METHOD 02---------------------#
