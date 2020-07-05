# ---------------------- PROBLEM 16 (RANDOM) ----------------------------------#
# Write a function called factorial which accepts a number and returns the factorial 
# of that number. A factorial is the product of an integer and all the intergers below it; 
# e.g. factorial four (4!) is equal to 24, because 4 * 3 * 2 * 1 equals 24.

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def factorial(number):

	if number == 0: return 1

	return number * factorial(number - 1)
# ----------------METHOD 01---------------------#