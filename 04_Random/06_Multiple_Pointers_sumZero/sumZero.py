# ---------------------- PROBLEM 06 (RANDOM) ----------------------------------#
# Write a function called sumZero, which accepts a sorted array of integers.
# The function should find the first pair where the sum is 0. Return an array that
# includes both values that sum to zero or undefined if pair doesn't exist.

# Assumption: Input Array is sorted
# Sample input: [-3, -2, -1, 0, 1, 2, 3]
# Sample output: [-3, 3]

# Sample input: [-2, 0, 1, 3]
# Sample output: undefined

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def sumZero(arr):
	# iterate over pairs 
	for i in range(0, len(arr)):
		first_ptr = i
		for j in range(i + 1, len(arr)):
			sec_ptr = j
			sum_nums = arr[i] + arr[j]
			if sum_nums == 0:
				return [arr[i], arr[j]]
	return None
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = WORST/AVERAGE TIME: O(n), BEST TIME: O(1), SPACE: O(1)
def sumZero(arr):
	# define two pointer
	left = 0
	right = len(arr) - 1

	while left < right:
		first_num = arr[left]
		sec_num = arr[right]
		sum_nums = first_num + sec_num
		if sum_nums == 0:
			return [first_num, sec_num]
		elif sum_nums < 0:
			left += 1
		else:
			right -= 1
	return None
# ----------------METHOD 02---------------------#