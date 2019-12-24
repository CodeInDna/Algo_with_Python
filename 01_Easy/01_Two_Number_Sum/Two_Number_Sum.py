# ---------------------------------- PROBLEM 01 (EASY) ----------------------------------------------#
# Write a function that takes in a non-empty array of distinct integers and an integer representing a 
# target sum. If any two numbers in the input array sum up to the target sum, the function should 
# return them in an array, in sorted order. If no two numbers sum up to the target sum, the function 
# should return an empty array. Assume that there will be at most one pair of numbers summing up to the 
# target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
# Sample output: [-1, 11]
# Assumption: 
	# * Input list : Non-Empty
	# * Input list : Distinct numbers
	# * Input list :At most one pair of numbers summing up to the target sum

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n ^ 2), SPACE: O(1) 
def two_number_sum(lst, target):
	for i in range(len(lst)):
		firstNum = lst[i]
		for j in range(i+1, len(lst)):
			secondNum = lst[j]
			if firstNum + secondNum == target:
				return sorted([firstNum, secondNum])
	return []
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def two_number_sum(lst, target):
	visited = []
	for num in lst:
		diff = target - num
		if diff in visited:
			return sorted([num, diff])
		visited.append(num)
	return []

print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# ----------------METHOD 02---------------------#


# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(nlog(n)), SPACE: O(1) 
def two_number_sum(lst, target):
	lst.sort()
	left_pointer = 0
	right_pointer = len(lst) - 1
	while left_pointer < right_pointer:
		add = lst[left_pointer] + lst[right_pointer]
		if add == target:
			return [lst[left_pointer], lst[right_pointer]]
		elif add < target:
			left_pointer += 1
		elif add > target:
			right_pointer -= 1
	return []
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# ----------------METHOD 03---------------------#

		
