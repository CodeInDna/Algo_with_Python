# --------------------------- PROBLEM 22 (HARD)-------------------------------#
# Longest Substring Without Duplication

# Write a function that takes in a string and that returns its longest substring without duplicate characters. 
# Assume that there will only be one longest substring without duplication.

# Sample input: "clementisacap"
# Sample output: "mentisac"

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
# n^2 : n-index() | n-while and sliding window
def longestSubstringWithoutDuplication(string):
	if len(string) <= 1:
		return string

	start_idx = 0
	end_idx = 1

	longest_substr = ''

	while(end_idx != len(string)):
		char_to_compare = string[end_idx]
		string_to_look = string[start_idx:end_idx]

		if char_to_compare not in string_to_look:
			if len(string_to_look+char_to_compare) > len(longest_substr):
				longest_substr = string_to_look + char_to_compare
			end_idx += 1
		else:
			idx_dup_found = start_idx + string_to_look.index(char_to_compare)
			start_idx = idx_dup_found + 1
			
	return longest_substr
	
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(min(n, a))	
# n : length of the string | a: set of unique letters in our string
def longestSubstringWithoutDuplication(string):
	if len(string) <= 1:
		return string

	start_idx = 0 
	longest_substr = ''
	last_seen = {}
	for i, char in enumerate(string):
		string_to_look = string[start_idx:i]

		if char in string_to_look:
			start_idx = last_seen[char] + 1
		elif len(longest_substr) <= len(string_to_look+char):
			longest_substr = string_to_look + char
		last_seen[char] = i 
	return longest_substr
# ----------------METHOD 02---------------------#

# print(longestSubstringWithoutDuplication('clementisacap'))