# ---------------------- PROBLEM 04 (RANDOM) ----------------------------------#
# Write a function called sameFrequency. Given two positive numbers, find out 
# if the two numbers have the same frequency of digits

# Sample input: 128, 281
# Sample output: True

# Sample input: 22, 2222
# Sample output: False

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def sameFrequency(num1, num2):
	return sorted(str(num1)) == sorted(str(num2))
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(1), SPACE: O(n)
def sameFrequency(num1, num2):
	obj_num1 = {num: str(num1).count(num) for num in set(str(num1))}
	obj_num2 = {num: str(num2).count(num) for num in set(str(num2))}
	return obj_num1 == obj_num2
# ----------------METHOD 02---------------------#