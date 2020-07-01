# ---------------------- PROBLEM 11 (RANDOM) ----------------------------------#
# Given a sorted array of integers, write a function called search, that accepts 
# a value and return the index where the value passed to the function is located.
# If the value is not found, return -1

# Sample input: [1, 2, 3, 4, 5, 6], 4
# Sample output: 3

# ----------------METHOD 01---------------------#
# Linear Search
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	return -1
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(logn), SPACE: O(1)
def search(arr, target):
	left = 0
	right = len(arr) - 1
	while left <= right:
		middle = (left + right) // 2
		num = arr[middle]
		if num == target:
			return middle
		elif num > target:
			right = middle - 1
		else:
			left = middle + 1
	return -1
# ----------------METHOD 02---------------------#