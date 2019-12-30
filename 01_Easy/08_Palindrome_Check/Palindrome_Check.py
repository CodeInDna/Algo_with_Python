# ---------------------------------- PROBLEM 08 (EASY) --------------------------------------#
# Palindrome Check
# Write a function that takes in a non-empty string and that returns a boolean representing 
# whether or not the string is a palindrome. A palindrome is defined as a string that is written 
# the same forward and backward.

# Sample input: "abcdcba"
# Sample output: True (it is a palindrome)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2) as we are iterating a string everytime we are performing concatenation
# , SPACE: O(n) 
def isPalindrome(str):
	new_str = ''
	for i in range(len(str)-1, -1, -1):
		new_str += str[i]
	return str == new_str
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) as we are creating a new string of length same as the given string
def isPalindrome(str):
	reversedString = []
	for i in range(len(str)-1, -1, -1):
		reversedString.append(str[i])
	return str == ''.join(reversedString)
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n/2), we can say O(n), SPACE: O(1)
def isPalindrome(str):
	left = 0
	right = len(str)-1
	while left <= right:
		if str[left] != str[right]:
			return False
		left += 1	
		right -= 1	
	return True
# ----------------METHOD 03---------------------#

# ----------------METHOD 04---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def isPalindrome(str):
	return str == str[::-1]
print(isPalindrome("abcdcba"))
# ----------------METHOD 04---------------------#

# ----------------METHOD 05---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def isPalindrome(str, i = 0):
	j = len(str) - 1 -i
	if i >= j:
		return True
	else:
		return str[i] == str[j] and isPalindrome(str, i+1)
# ----------------METHOD 05---------------------#

print(isPalindrome('abcdcba'))
print(isPalindrome('ab'))
print(isPalindrome('abcdefghijjihgfedcba'))