# ---------------------------------- PROBLEM 22 (MEDIUM) --------------------------------------#
# Longest Palindromic Substring

# Write a function that, given a string, returns its longest palindromic substring. A palindrome is 
# defined as a string that is written the same forward and backward. Assume that there will only be 
# one longest palindromic substring.

# Sample input: "abaxyzzyxf"
# Sample output: "xyzzyx"

# ----------------METHOD 01---------------------#
# TOTAL: COMPLEXITY = TIME: O(n^3), SPACE: O(1)
# INDIVIDUAL COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def longestPalindromicSubstring(string):
	longestPal = ''
	for i in range(len(string)):
		for j in range(i, len(string)):
			substr = string[i:j + 1]
			if isPalindrome(substr) and len(substr) > len(longestPal):
				longestPal = substr
	return longestPal

# INDIVIDUAL COMPLEXITY = TIME: O(n), SPACE: O(1)
def isPalindrome(string):
	if string == string[::-1]:
		return True
	return False
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# INDIVIDUAL COMPLEXITY = TIME: O(n), SPACE: O(1)
def isPalindrome(string):
	leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# TOTAL COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def longestPalindromicSubstring(string):
	currentLongest = [0, 1]
	for i in range(len(string)): 
		odd = getLongestPalindromeFrom(string, i-1, i+1)
		even = getLongestPalindromeFrom(string, i-1, i)
		longest = max(odd, even, key = lambda x:x[1] - x[0])
		currentLongest = max(longest, currentLongest, key = lambda x:x[1] - x[0])
		print(odd, even, longest, currentLongest)
	return string[currentLongest[0]:currentLongest[1]]
		
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]
# ----------------METHOD 03---------------------#