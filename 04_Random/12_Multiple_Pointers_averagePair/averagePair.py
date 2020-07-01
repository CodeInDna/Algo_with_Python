# ---------------------- PROBLEM 12 (RANDOM) ----------------------------------#
# Write a function called averagePair. Given a sorted array of integers and a 
# target average, determine if there is a pair of values in the array where the
# average of the pair equals the target average. There may be more than one pair 
# that matches the average target.

# Sample input: [1,3,3,5,6,7,10,12,19], 8
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def averagePair(arr, target_avg):
	for i in range(len(arr)):
		num1 = arr[i]
		for j in range(i+1, len(arr)):
			num2 = arr[j]
			avg = num1 + num2 / 2
			if avg == target_avg:
				return True
	return False
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# Multiple Pointers
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def averagePair(arr, target_avg):
	left = 0
	right = len(arr) - 1
	while left <= right:
		num1 = arr[left]
		num2 = arr[right]
		avg = num1 + num2 / 2
		if avg == target_avg:
			return True
		elif avg > target_avg:
			right -= 1
		else:
			left += 1
	return False
# ----------------METHOD 02---------------------#