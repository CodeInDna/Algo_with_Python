# ---------------------------------- PROBLEM 01 (RANDOM) ----------------------------------------------#
# Write a function that takes in a string and return count of each charcter in 
# the string. Assume allowed characters can only be alphabets and numbers.

# Sample input: 'aaaa'
# Sample output: {a: 4}

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if type(string) != str: return False
	if not string: return False

	# define an object to return in the end
	charCount = {}

	# iterate over the lowercase characters 
	for char in string.lower():
	# check if char is alphanumeric
		if char.isalnum(): 
		# if char not in object, initialize it with 1, else add 1
			charCount[char] = charCount[char] + 1 if char in charCount else 1

	# return object with char count
	return charCount
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if type(string) != str: return False
	if not string: return False

	# define an object to return in the end
	str_lower = string.lower()

	charCount = {char: str_lower.count(char) for char in set(str_lower) if char.isalnum()}
	
	# return object with char count
	return charCount
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if type(string) != str: return False
	if not string: return False

	# define an object to return in the end
	str_lower = string.lower()

	# define an object to return at the end
	charCount = {}

	for key in str_lower:
		if check_alnum(key):
			charCount[key] = charCount.get(key, 0) + 1
	
	# return object with char count
	return charCount

import re
def check_alnum(char):
	return bool(re.match('^[a-zA-Z0-9]+$', char))
	# if ord(char) > 96 and ord(char) < 123: return True
	# if ord(char) > 64 and ord(char) < 91: return True
	# if ord(char) > 47 and ord(char) < 58: return True
	# return False
# ----------------METHOD 03---------------------#

from collections import Counter
# ----------------METHOD 04---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if type(string) != str: return False
	if not string: return False

	charCount = Counter(keep_alnum(string.lower()))
	
	# return object with char count
	return charCount

def keep_alnum(string):
	string = re.sub(r'[^A-Za-z0-9]+', '', string)
	return string
# ----------------METHOD 04---------------------#


