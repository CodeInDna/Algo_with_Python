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
print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(), SPACE: O()

# ----------------METHOD 02---------------------#
