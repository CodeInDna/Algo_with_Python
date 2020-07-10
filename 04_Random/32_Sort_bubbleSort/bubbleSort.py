# ---------------------- PROBLEM 32 (RANDOM) ----------------------------------#
# Write a function called bubbleSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def bubbleAscSort(arr):
	for i in reversed(range(1, len(arr))):
		for j in range(1, i+1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return arr
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def bubbleDescSort(arr):
	for i in reversed(range(1, len(arr))):
		for j in range(1, i+1):
			if arr[j] > arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return arr
# ----------------METHOD 02---------------------#

print(bubbleAscSort([5, 3, 4, 1, 2]))
print(bubbleDescSort([5, 3, 4, 1, 2]))