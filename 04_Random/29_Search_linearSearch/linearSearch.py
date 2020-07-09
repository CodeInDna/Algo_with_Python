# ---------------------- PROBLEM 29 (RANDOM) ----------------------------------#
# Write a function called linearSearch which accepts an array and a number and 
# if the number is present in the array return index else return None.

# Sample input: [3,4,51,10,32,12,10], 10
# Sample output: 3

# ----------------METHOD 01---------------------#
# COMPLEXITY = WORST/AVERAGE CASE TIME: O(n), BEST CASE TIME: O(1), SPACE: O(1)
def linearSearch(arr, target):
	for i in range(len(arr)):
		if arr[i] == target: return i
	return None
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = WORST/AVERAGE CASE TIME: O(n), BEST CASE TIME: O(1), SPACE: O(1)
def linearSearch(arr, target):
	return arr.index(target) if target in arr else None 
# ----------------METHOD 02---------------------#

print(linearSearch([3,4,51,10,32,12,10], 10))
print(linearSearch([3,4,51,10,32,12,10], 1))