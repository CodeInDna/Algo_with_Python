# ---------------------- PROBLEM 19 (RANDOM) ----------------------------------#
# Write a function called fib which accepts a number and returns the nth number
# in the Fibonacci sequence. Recall that the Fibonacci sequence of whole numbers
# 1,1,2,3,5,8...which starts with 1 and 1, and where every number therafter is 
# equal to the sum of the precious two numbers.

# Sample input: 10
# Sample output: 55

# RECURSION
# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(2^n), SPACE: O(1)
def fib(number):
	if number <= 2: return 1

	return fib(number-1) + fib(number-2)
# ----------------METHOD 01---------------------#

# ITERTIVE
# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def fib(number):
	a=1
	b=1
	z=0
	for i in range(number-2):
		z = a+b
		a, b = b, z
	return z	
# ----------------METHOD 02---------------------#

# DYNAMIC PROGRAMMING (Memoization)
# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def fib(number, memo={1:1, 2:1}):
	if number in memo.keys(): return memo[number]

	res = fib(number-1) + fib(number-2)
	memo[number] = res

	return res
# ----------------METHOD 03---------------------#

# DYNAMIC PROGRAMMING (Tabulation/BottomUp Approach)
# ----------------METHOD 04---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def fib(number):
	if number <= 2: return 1
	fibNums = [1, 1]
	for i in range(2, number):
		fibNums.append(fibNums[i-1] + fibNums[i-2])
	return fibNums[number-1]
# ----------------METHOD 04---------------------#
print(fib(6))