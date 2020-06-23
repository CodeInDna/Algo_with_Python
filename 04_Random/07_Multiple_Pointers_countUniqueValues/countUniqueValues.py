# ---------------------- PROBLEM 07 (RANDOM) ----------------------------------#
# Implement a function called countUniqueValues which accepts a sorted array, and
# counts the unique values in the array. There can be negative numbers in the
# array, but it will always be sorted.

# Assumption: The numbers in array are always sorted

# Sample input: [1, 1, 1, 1, 1, 2]
# Sample output: 2

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def countUniqueValues(arr):
	if len(arr) == 0: return 0

	# define first pointer
	ptr_1 = 0

	# for each pair of pointer
	for ptr_2 in range(1, len(arr)):
		num1, num2 = arr[ptr_1], arr[ptr_2]
		# check if both are different
		if num1 != num2:
			# if different: increment first pointer
			ptr_1 += 1
			# replace its value with the value where the second pointer is
			arr[ptr_1] = num2

	return ptr_1 + 1
# ----------------METHOD 01---------------------#

# Alternate Mthods without Multiple Pointers
# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def countUniqueValues(arr):
	# if the arr is empty return None
	if len(arr) == 0: return 0

	# define a variable to keep counter and store the number
	count = 1
	num = arr[0]

	for i in range(1, len(arr)):
		curr_num = arr[i]
		if curr_num != num:
			count += 1
			num = curr_num
	return count
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(1), SPACE: O(1)
def countUniqueValues(arr):

	return len(set(arr))
# ----------------METHOD 03---------------------#