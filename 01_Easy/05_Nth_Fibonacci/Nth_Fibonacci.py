# ---------------------------------- PROBLEM 05 (EASY) --------------------------------------#
# Nth Fibonacci
# The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the 
# second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. 
# Write a function that takes in an integer n and returns the nth Fibonacci number.

# Sample input: 6
# Sample output: 5 (0, 1, 1, 2, 3, 5)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def getNthFib(n):
	a = 0
	b = 1
	if n == 1:
		return 0
	if n == 2:
		return 1
	for i in range(n-2):
		z = a + b
		a = b
		b = z
	return z
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(2^n), SPACE: O(n)
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n - 1) + getNthFib(n - 2)
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def getNthFib(n, memoize = {1: 0, 2: 1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
		# print(memoize[n])
		return memoize[n]

print(getNthFib(6))
print(getNthFib(9))
print(getNthFib(7))
print(getNthFib(1))
print(getNthFib(2))
# ----------------METHOD 03---------------------#