# ---------------------- PROBLEM 15 (RANDOM) ----------------------------------#
# Write a function called power which accepts a base and an exponent. The function
# should return the power of the base to the exponent. This function should mimic 
# the functionality of Math.pow() - do not worry about negative bases and exponents.

# Sample input: 2, 0
# Sample output: 1

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def power(base, exp):

	if exp == 0: return 1

	return base * power(base, exp-1)
# ----------------METHOD 01---------------------#