# ---------------------- PROBLEM 03 (RANDOM) ----------------------------------#
# Given two strings, write a function to determine if the second string is an
# anagram of the first. An anagram is a word, aphrase, or a name formed by rearranging
# the letters of another, such as cinema formed from iceman

# Assumption: The strings only contains lowercase letters

# Sample input: 'anagram', 'nagaram'
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), BEST CASE SPACE: O(logn), WORST/AVERAGE SPACE: O(n)
def validAnagrams(str1, str2):

	# if both are of different length, return False
	if len(str1) != len(str2): return False

	str_obj1 = {}
	str_obj2 = {}

	for char in str1:
		if char in str_obj1:
			str_obj1[char] += 1
		else:
			str_obj1[char] = 1

	for char in str2:
		if char in str_obj2:
			str_obj2[char] += 1
		else:
			str_obj2[char] = 1

	return str_obj1 == str_obj2
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def validAnagrams(str1, str2):

	# if both are of different length, return False
	if len(str1) != len(str2): return False

	return sorted(str1) == sorted(str2)
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
from collections import Counter
def validAnagrams(str1, str2):

	# if both are of different length, return False
	if len(str1) != len(str2): return False

	return Counter(str1) == Counter(str2)
# ----------------METHOD 03---------------------#