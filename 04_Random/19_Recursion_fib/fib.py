# ---------------------- PROBLEM 19 (RANDOM) ----------------------------------#
# Write a function called fib which accepts a number and returns the nth number
# in the Fibonacci sequence. Recall that the Fibonacci sequence of whole numbers
# 1,1,2,3,5,8...which starts with 1 and 1, and where every number therafter is 
# equal to the sum of the precious two numbers.

# Sample input: 10
# Sample output: 55

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def fib(number):
	if number <= 2: return 1

	return fib(number-1) + fib(number-2)
# ----------------METHOD 01---------------------#
print(fib(28))