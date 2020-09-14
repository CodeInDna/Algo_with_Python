# ---------------------- PROBLEM 2 (RANDOM) ----------------------------------#
# Given a sorted array and a number, write a function called sortedFrequency that
# counts the occurrences of the number in the array.

# Sample input: [1,1,2,2,2,2,3], 2
# Sample output: 4

# ----------------METHOD 01---------------------#
# Using Divide and Conquer
# COMPLEXITY = TIME: O(), SPACE: O()
def occurrenceSearch(lst, num, SearchFirst):
	left = 0
	right = len(arr) - 1

	result = -1

	while left <= right:
		mid = (left + right) // 2

		if num == arr[mid]:
			result = mid
			if SearchFirst:
				right = mid - 1
			else:
				left = mid + 1
		elif num < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return result
	
def sortedFrequency(arr, num):
	firstOccIdx = occurrenceSearch(arr, num, True)
	lastOccIdx = occurrenceSearch(arr, num, False)
	length = lastOccIdx - firstOccIdx + 1
	return length
# ----------------METHOD 01---------------------#

print(sortedFrequency([1,2,2,2,2,3,3,4],2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3], 2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3], 3)) # 1
print(sortedFrequency([1,1,2,2,2,2,3], 1)) # 2
print(sortedFrequency([1,1,2,2,2,2,3], 4)) # -1