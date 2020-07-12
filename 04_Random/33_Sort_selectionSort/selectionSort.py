# ---------------------- PROBLEM 33 (RANDOM) ----------------------------------#
# Write a function called selectionSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx =  j
		arr[min_idx], arr[i] = arr[i], arr[min_idx]
	return arr
# ----------------METHOD 01---------------------#