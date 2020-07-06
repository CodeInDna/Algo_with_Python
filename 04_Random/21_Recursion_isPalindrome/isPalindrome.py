# ---------------------- PROBLEM 21 (RANDOM) ----------------------------------#
# Write a function called isPalindrome which returns true if the string passed
# to it is a palindrome (reads the same forward and backward). Otherwise it
# returns false.

# Sample input: 'tacocat'
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def isPalindrome(string):
	if len(string) == 0: return False
	if len(string) == 1: return True
	if len(string) == 2: return string[0] == string[-1]
	return isPalindrome(string[1:-1]) if string[0] == string[-1] else False 
# ----------------METHOD 01---------------------#
