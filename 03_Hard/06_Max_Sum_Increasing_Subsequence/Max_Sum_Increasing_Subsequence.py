# ---------------------------------- PROBLEM 6 (HARD) --------------------------------------#
# Max Sum Increasing Subsequence

# Given an non-empty array of integers, write a function that returns an array of length 2. The 
# first element in the output array should be an integer value representing the greatest sum that 
# can be generated from a strictly-increasing subsequence in the array. The second element should 
# be an array of the numbers in that subsequence. A subsequence is defined as a set of numbers that 
# are not necessarily adjacent but that are in the same order as they appear in the array. Assume 
# that there will only be one increasing subsequence with the greatest sum.

# Sample input: [10, 70, 20, 30, 50, 11, 30]
# Sample output: [110, [10, 20, 30, 50]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n^2), n is the length of given list of numbers
def maxSumIncreasingSubsequence(lst):
	sums = lst[:]
	sequences = [None] * len(lst)
	maxSumIdx = 0
	for i in range(len(lst)):
		currNum = lst[i]
		for j in range(i):
			otherNum = lst[j]
			if (otherNum < currNum) and (currNum + sums[j] >= sums[i]):
				sums[i] = sums[j] + currNum
				sequences[i] = j
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i

	return [sums[maxSumIdx], buildSequence(lst, sequences, maxSumIdx)]

def buildSequence(lst, sequences, currIdx):
	sequence = []
	while currIdx is not None:
		sequence.append(lst[currIdx])
		currIdx = sequences[currIdx]
	return sequence[::-1]
# ----------------METHOD 01---------------------#