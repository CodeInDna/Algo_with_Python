# ---------------------------------- PROBLEM 01 (RANDOM) ----------------------------------------------#
# Write a function that takes in a string and return count of each charcter in 
# the string

# Sample input: 'aaaa'
# Sample output: {a: 4}

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
# def char_count(string):
# 	# if string is empty return False
# 	if not string: return False

# 	# define an object to return in the end
# 	charCount = {}

# 	# iterate over the lowercase characters 
# 	for char in string.lower():
# 	# check if char is alphanumeric
# 		if char.isalnum(): 
# 		# if char not in object, initialize it with 1, else add 1
# 			charCount[char] = charCount[char] + 1 if char in charCount else 1

# 	# return object with char count
# 	return charCount
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if not string: return False

	# define an object to return in the end
	str_lower = string.lower()

	charCount = {char: str_lower.count(char) for char in str_lower if char.isalnum()}
	
	# return object with char count
	return charCount
# ----------------METHOD 02---------------------#