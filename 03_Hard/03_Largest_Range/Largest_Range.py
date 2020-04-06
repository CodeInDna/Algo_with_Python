# ---------------------------------- PROBLEM 3 (HARD) --------------------------------------#
# Largest Range

# Write a function that takes in an array of integers and returns an array of length 2 representing 
# the largest range of numbers contained in that array. The first number in the output array should be 
# the first number in the range while the second number should be the last number in the range. A range 
# of numbers is defined as a set of numbers that come right after each other in the set of real integers. 
# For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. 
# Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume 
# that there will only be one largest range.

# Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# Sample output: [0, 7]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
from collections import defaultdict
def largestRange(lst):
	longestLength = 0
	ref_dict = dict.fromkeys(lst, True)
	bestRange = []
	for num in lst:
		# if value of a number is False, skip it
		if not ref_dict[num]:
			continue
		# Visit the number
		ref_dict[num]= False
		
		currentLength = 1
		left = num - 1
		right = num + 1

		while left in ref_dict:
			ref_dict[left] = False
			left -= 1
			currentLength += 1

		while right in ref_dict:
			ref_dict[right] = False
			right += 1
			currentLength += 1

		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left + 1, right - 1]

	return bestRange
# ----------------METHOD 01---------------------#
