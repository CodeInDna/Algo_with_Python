# ---------------------------------- PROBLEM 18 (MEDIUM) --------------------------------------#
# Permutations

# Write a function that takes in an array of unique integers and returns an array of all permutations 
# of those integers. If the input array is empty, your function should return an empty array.

# Sample Input: [1,2,3]
# Sample output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def getPermutations(array):
	permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, currentpermutation, permutations):
	if not len(array) and len(currentpermutation):
		permutations.append(currentpermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i + 1:]
			newPermutations = currentpermutation + [array[i]]
			permutationsHelper(newArray, newPermutations, permutations)
# ----------------METHOD 01---------------------#
