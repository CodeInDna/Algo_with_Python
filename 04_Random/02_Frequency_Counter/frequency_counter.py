# ---------------------- PROBLEM 02 (RANDOM) ----------------------------------#
# Write a function called same, which accepts two arrays. The function should 
# return true if every value in the array has it's corresponding value squared 
# in the second array. The frequncy of values must be the same

# Sample input: [1, 2, 3], [1, 9, 4]
# Sample output: True

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def same(arr1, arr2):
	# check the length of both array
	if len(arr1) != len(arr2): return False

	# Iterate over each element in array 1
	for num in arr1:  # Time Complexity = O(n)
	# if element's squared value is not in array 2 return False
		if num**2 not in arr2: 
			return False
	# else remove that element from array 2
		else:
			arr2.remove(num**2)	# remove() : Time Complexity = O(n)
	# if all conditions passed, return True
	return True
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# BEST CASE: COMPLEXITY = TIME: O(n), SPACE: O(1)
# WORST/ AVERAGE CASE: COMPLEXITY = TIME: O(n log n), SPACE: O(1)
def same(arr1, arr2):
	# check the length of both array
	if len(arr1) != len(arr2): return False

	# sort both arrays and equate them (Squared the first one)
	return sorted(arr2) == sorted([num**2 for num in arr1])
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE WORST/AVERAGE: O(n), BEST: O(log n)
def same(arr1, arr2):
	# check the length of both array
	if len(arr1) != len(arr2): return False

	# create an object to store frequency of numbers in array 2
	squared_dict = {num: arr2.count(num) for num in set(arr2)}

	for num in arr1:
		if squared_dict[num**2] != arr1.count(num):
			return False
	return True
# ----------------METHOD 03---------------------#