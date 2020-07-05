# ---------------------- PROBLEM 10 (RANDOM) ----------------------------------#
# Write a function called findLongestSubstring, which accepts a string and returns the
# length of the longest substring with all distinct characters.

# Sample input: 'thisisawesome'
# Sample output: 6

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def findLongestSubstring(string):
	start = 0
	maxLen = 0
	seen = {}

	for end in range(len(string)):
		if string[end] in seen:
			start = max(start, seen[string[end]] + 1)
		maxLen = max(maxLen, end - start + 1)
		seen[string[end]] = end
	return maxLen
# ----------------METHOD 01---------------------#