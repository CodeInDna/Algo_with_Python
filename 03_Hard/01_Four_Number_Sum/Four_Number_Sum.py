# ---------------------------------- PROBLEM 1 (HARD) --------------------------------------#
# Four Number Sum

# Write a function that takes in a non-empty array of distinct integers and an integer representing 
# a target sum. The function should find all quadruplets in the array that sum up to the target sum 
# and return a two-dimensional array of all these quadruplets in no particular order. If no four numbers 
# sum up to the target sum, the function should return an empty array.

# Sample input: [7, 6, 4, -1, 1, 2], 16
# Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]

# ----------------METHOD 01---------------------#
# AVERAGE COMPLEXITY = TIME: O(n^2), SPACE: O(n^2) 
# WORST COMPLEXITY = TIME: O(n^3), SPACE: O(n^2) 
def fourNumberSum(lst, target):
	pair_tracker = {}
	quadruplets = []
	for i in range(1, len(lst)-1):
		for j in range(i+1, len(lst)):
			x = lst[i]
			y = lst[j]
			P = x+y
			diff = target - P
			if diff in pair_tracker:
				for pair in pair_tracker[diff]:
					quadruplets.append(pair + [lst[i], lst[j]])
		for k in range(0, i):
			currSum = lst[i] + lst[k]
			if currSum not in pair_tracker:
				pair_tracker[currSum] = [[lst[k], lst[i]]]
			else:
				pair_tracker[currSum].append([lst[k], lst[i]])
	return quadruplets
# ----------------METHOD 01---------------------#
print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))