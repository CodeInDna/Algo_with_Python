# ---------------------- PROBLEM 37 (RANDOM) ----------------------------------#
# Write a function called radixSort which accepts an array return the sorted array 
# in ascending order.

# Sample input: [5, 3, 4, 1, 2]
# Sample output: [1, 2, 3, 4, 5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(nk), SPACE: O(n + k), n: numbers in array, k: digits in numbers
def getDigits(num, place):
	return abs(num) // 10**place % 10

def digitCount(num):
	return len(str(abs(num)))

def maxDigits(lst):
	if len(lst) == 0: return 0
	return digitCount(max(lst))

def radixSort(arr):
	maxDig = maxDigits(arr)
	for place in range(maxDig):
		bucket = [[] for _ in range(10)]
		for num in arr:
			x = getDigits(num, place)
			bucket[x].append(num)
		arr = [item for sublist in bucket for item in sublist]
	return arr
# ----------------METHOD 01---------------------#

