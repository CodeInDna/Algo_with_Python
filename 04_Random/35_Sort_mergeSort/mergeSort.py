# ---------------------- PROBLEM 33 (RANDOM) ----------------------------------#
# Write a function called mergeSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(nlogn), SPACE: O(n)
def mergeHelper(arr1, arr2):
	i = 0
	j = 0
	newArr = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			newArr.append(arr1[i])
			i += 1
		else:
			newArr.append(arr2[j])
			j += 1
	if i < len(arr1):
		newArr += arr1[i:]
	elif j < len(arr2):
		newArr += arr2[j:]
	return newArr

def mergeSort(arr):
	if len(arr) <= 1: return arr

	mid = len(arr) // 2

	return mergeHelper(mergeSort(arr[:mid]), mergeSort(arr[mid:])) 
# ----------------METHOD 01---------------------#
