# ---------------------- PROBLEM 1 (RANDOM) ----------------------------------#
# Given an array of 1s and 0s which has all 1s first followed by all 0s, write a
# function called countZeros, which returns the number of zeros in the array.

# Sample input: [1,1,1,1,0,0]
# Sample output: 2

# ----------------METHOD 01---------------------#
# Using Divide and Conquer
# COMPLEXITY = TIME: O(logn), SPACE: O(1)
def countZeros(lst):
	left = 0
	right = len(lst) - 1
	if lst[left] == 1 and lst[right] == 1:
		return 0
	if lst[left] == 0 and lst[right] == 0:
		return len(lst)
	while left < right:
		mid = (left + right) // 2
		if lst[mid] == 1:
			left = mid + 1
		elif lst[mid] == 0:
			right = mid
	return len(lst) - right
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def countZeros(lst):
	return lst.count(0)
# ----------------METHOD 02---------------------#

print(countZeros([1,1,1,1]))
print(countZeros([0,0,0,0,0]))
print(countZeros([1,1,1,1,0,0]))
print(countZeros([1,1,0,0,0,0,0,0]))