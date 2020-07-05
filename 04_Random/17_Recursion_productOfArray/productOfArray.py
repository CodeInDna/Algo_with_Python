# ---------------------- PROBLEM 17 (RANDOM) ----------------------------------#
# Write a function called productOfArray which takes in an array of numbers and 
# return the product of them all.

# Sample input: [1,2,3]
# Sample output: 6

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def productOfArray(arr):
	if len(arr) == 0:
		return 1

	return arr[0] * productOfArray(arr[1:])
# ----------------METHOD 01---------------------#


print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))