# ---------------------- PROBLEM 22 (RANDOM) ----------------------------------#
# Write a function called some Recursive which accepts an array and a callback.
# The function returns true if a single value in the array returns true when passed
# to the callback.Otherwise it return false.

# Sample input: [1,2,3,4], isOdd
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)

def isOdd(num): return True if num % 2 != 0 else False 

def someRecursive(arr, callback):
	if len(arr) == 0: return False
	if callback(arr[0]): return True
	return someRecursive(arr[1:], callback)
# ----------------METHOD 01---------------------#
