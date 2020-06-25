# ---------------------- PROBLEM 08 (RANDOM) ----------------------------------#
# Write a function called maxSubarraySum which accepts an array of integers and
# a number called n. The function should calculate the maximum sum of n consecutive 
# elements in the array.

# Sample input: [1, 2, 5, 2, 8, 1, 5], 2
# Sample output: 10

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def maxSubarraySum(arr, num):

	if len(arr) < num: return None

	# define a variable which holds the max Sum
	maxSum = float("-inf")

	# iterate over each number
	for i in range(len(arr) - num + 1):
		total = arr[i]
		# iterate till the range given
		for j in range(i+1, i+num):
			total += arr[j]
		# compare the summation with maxSum, replace if sum is large
		maxSum = max(maxSum, total)
	return maxSum
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def maxSubarraySum(arr, num):
	if len(arr) < num: return None

	subArraySum = sum(arr[0:num])
	maxSum = subArraySum

	for i in range(num, len(arr)):
		subArraySum = subArraySum + arr[i] - arr[i - num]
		maxSum = max(maxSum, subArraySum)
	return maxSum
# ----------------METHOD 02---------------------#