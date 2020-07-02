# ---------------------- PROBLEM 12 (RANDOM) ----------------------------------#
# Write a function called isSubsequence which takes in two strings and checks whether
# the characters in the first string form a subsequence of the characters in the 
# second string. In other words, the function should check whether the characters
# in the first string appear somewhere in the second string, without their order changing.

# Sample input: 'hello', 'hello_world'
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def isSubsequence(str1, str2):
	str1_idx = 0
	str2_idx = 0
	while str2_idx < len(str2):
		if str1[str1_idx] == str2[str2_idx]:
			str1_idx += 1
		if str1_idx == len(str1): return True
		str2_idx += 1
	return False
# ----------------METHOD 01---------------------#