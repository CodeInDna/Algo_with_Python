# ---------------------------------- PROBLEM 7 (HARD) --------------------------------------#
# Longest Common Subsequence

# Implement a function that returns the longest subsequence common to two given strings. A subsequence 
# is defined as a group of characters that appear sequentially, with no importance given to their 
# actual position in a string. In other words, characters do not need to appear consecutively in 
# order to form a subsequence. Assume that there will only be one longest common subsequence.

# Sample input: "ZXVVYZW", "XKYKZPW"
# Sample output: ["X", "Y", "Z", "W"]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(nm * min(n, m)), SPACE: O(nm * min(n, m)), n, m are the length of str1 and str2 resp.
def longestCommonSubsequence(str1, str2):
	lcs =[[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
			else:
				lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j], key = len)
	return lcs[-1][-1]
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(nm), SPACE: O(nm), because we are not appending two list like in line 19
def longestCommonSubsequence(str1, str2):
	lcs =[[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				lcs[i][j] = lcs[i - 1][j - 1] + 1
			else:
				lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
	return buildSequence(lcs, str1)

def buildSequence(lengths, string):
	sequence = []
	i = len(lengths) - 1
	j = len(lengths[0]) - 1
	while i != 0 and j != 0:
		if lengths[i][j] == lengths[i][j - 1]:
			j -= 1
		elif lengths[i][j] == lengths[i - 1][j]:
			i -= 1
		else:
			sequence.append(string[j - 1])
			i -= 1
			j -= 1
	return sequence[::-1]
# ----------------METHOD 02---------------------#