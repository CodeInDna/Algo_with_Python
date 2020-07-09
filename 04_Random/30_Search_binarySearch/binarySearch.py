# ---------------------- PROBLEM 30 (RANDOM) ----------------------------------#
# Write a function called binarySearch which accepts an array and a number and 
# if the number is present in the array return index else return None.

# Sample input: [3,4,51,10,32,12,10], 10
# Sample output: 3

# ----------------METHOD 01---------------------#
# COMPLEXITY = WORST/AVERAGE CASE TIME: O(n), BEST CASE TIME: O(1), SPACE: O(1)
def binarySearch(arr, target):
	arr = sorted(arr)
	left = 0
	right = len(arr) - 1
	while left <= right:
		middle = (left + right) // 2
		mid_num = arr[middle]
		if mid_num == target:
			return middle
		elif mid_num > target:
			right = middle - 1
		else:
			left = middle + 1
	return None
# ----------------METHOD 01---------------------#