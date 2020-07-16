# ---------------------- PROBLEM 36 (RANDOM) ----------------------------------#
# Write a function called quickSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(nlogn), SPACE: O(n)
def pivotHelper(arr):
	left = 0
	count = 0
	for j in range(1, len(arr)):
		if arr[left] > arr[j]:
			count += 1
			arr[count], arr[j] = arr[j], arr[count]
	arr[count], arr[left] = arr[left], arr[count]
	return count

def quickSort(arr):
	if len(arr) <= 1: return arr

	pivotIndex = pivotHelper(arr)

	left = quickSort(arr[:pivotIndex])
	right = quickSort(arr[pivotIndex+1:])

	return left + [arr[pivotIndex]] + right
# ----------------METHOD 01---------------------#

