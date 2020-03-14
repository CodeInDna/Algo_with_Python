# ---------------------------------- PROBLEM 19 (MEDIUM) --------------------------------------#
# Powerset

# Write a function that takes in an array of unique integers and returns its powerset. The powerset 
# P(X) of a set X is the set of all subsets of X. For example, the powerset of [1,2] is [[], [1], 
# [2], [1,2]]. Note that the sets in the powerset do not need to be in any particular order.

# Sample input: [1, 2, 3]

# Sample output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n*2^n), SPACE: O(n*2^n)
def powerset(arr):
	pow_set = [[]]
	for ele in arr:
		for j in range(len(pow_set)):
			currsubset = pow_set[j]
			pow_set.append(currsubset + [ele])
	return pow_set
print(powerset([1,2,3]))
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n*2^n), SPACE: O(n*2^n)
def powerset(array, idx=None):
	if idx is None:
		idx = len(array) - 1
	if idx < 0:
		return [[]]
	ele = array[idx]
	subsets = powerset(array, idx - 1)
	for j in range(len(subsets)):
		currsubset = subsets[j]
		subsets.append(currsubset + [ele])
	return subsets
print(powerset([1,2,3]))
# ----------------METHOD 02---------------------#

