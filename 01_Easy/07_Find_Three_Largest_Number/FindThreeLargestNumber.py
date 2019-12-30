# ---------------------------------- PROBLEM 06 (EASY) --------------------------------------#
# Find Three Largest Numbers
# Write a function that takes in an array of integers and returns a sorted array of the three 
# largest integers in the input array. Note that the function should return duplicate integers 
# if necessary; for example, it should return [10, 10, 12] for an input array of 
# [10, 5, 9, 10, 12].

# Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# Sample output: [18, 141, 541]

# ----------------METHOD 01---------------------#
# BEST CASE(sorted function): COMPLEXITY = TIME: O(n), SPACE: O(1)
# AVERAGE/WORST CASE(sorted function): COMPLEXITY = TIME: O(nlog(n)), SPACE: O(1)
def findThreeLargestNumbers(lst):
	sorted_lst = sorted(lst)
	return sorted_lst[-3:]
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def findThreeLargestNumbers(lst):
# Iterate over the given list
	threeLargestNums = [None, None, None]
	for num in lst:
		updateLargest(threeLargestNums, num)
	return threeLargestNums

def updateLargest(threeLargestNums, num):
# Check if the number is greater than the one of the three numbers in threeLargestNums list
	if threeLargestNums[2] is None or threeLargestNums[2] < num:
		shiftAndUpdate(threeLargestNums, num, 2)
	elif threeLargestNums[1] is None or threeLargestNums[1] < num:
		shiftAndUpdate(threeLargestNums, num, 1)
	elif threeLargestNums[0] is None or threeLargestNums[0] < num:
		shiftAndUpdate(threeLargestNums, num, 0)
	return threeLargestNums

def shiftAndUpdate(threeLargestNums, num, idx):
# Storing and Updating the number
	for i in range(idx + 1):
		if i == idx:
			threeLargestNums[i] = num
		else:
			threeLargestNums[i] = threeLargestNums[i+1]
	return threeLargestNums
# ----------------METHOD 02---------------------#

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))