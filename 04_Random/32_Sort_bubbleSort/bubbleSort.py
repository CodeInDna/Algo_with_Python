# ---------------------- PROBLEM 32 (RANDOM) ----------------------------------#
# Write a function called bubbleSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = WORST/AVERAGE TIME: O(n^2), BEST TIME(nearly sorted): O(n), SPACE: O(1)
def bubbleAscSort(arr):
	swap = False
	for i in reversed(range(1, len(arr))):
		for j in range(1, i+1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
				swap = True
		if not swap: return arr
	return arr
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = WORST/AVERAGE TIME: O(n^2), BEST TIME(nearly sorted): O(n), SPACE: O(1)
def bubbleDescSort(arr):
	for i in reversed(range(1, len(arr))):
		swap = False
		for j in range(1, i+1):
			if arr[j] > arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
				swap = True
		if not swap: return arr
	return arr
# ----------------METHOD 02---------------------#
