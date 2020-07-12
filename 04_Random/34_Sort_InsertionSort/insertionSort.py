# ---------------------- PROBLEM 32 (RANDOM) ----------------------------------#
# Write a function called insertionSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def insertionSort(arr):
	for i in range(1, len(arr)):
		j = i-1
		currVal = arr[i]
		while j >= 0 and arr[j] > currVal:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = currVal
	return arr 

# ----------------METHOD 01---------------------#
print(insertionSort([5,3,4,1,2]))