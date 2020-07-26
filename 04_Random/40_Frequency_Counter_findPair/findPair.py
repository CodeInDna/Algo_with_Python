# ---------------------- PROBLEM 03 (RANDOM) ----------------------------------#
# Given an unsorted array and a number n, find if there exists a pair of elements
# in the array whose difference is n. This function should return true if the pair 
# exists or false if it does not.

# Sample input: [6, 1, 4, 10, 2, 4], 2
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def findPair(arr, target):
	comp_lst = []
	for num in arr:
		sum_num = num + target
		if sum_num in comp_lst:
			return True
		comp_lst.append(num)
	return False
# ----------------METHOD 01---------------------#
