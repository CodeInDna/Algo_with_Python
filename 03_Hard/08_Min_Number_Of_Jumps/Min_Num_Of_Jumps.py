# ---------------------------------- PROBLEM 8 (HARD) --------------------------------------#
# Min Number Of Jumps

# You are given a non-empty array of integers. Each element represents the maximum number of steps 
# you can take forward. For example, if the element at index 1 is 3, you can go from index 1 to 
# index 2, 3, or 4. Write a function that returns the minimum number of jumps needed to reach the 
# final index. Note that jumping from index i to index i + x always constitutes 1 jump, no matter 
# how large x is.

# Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
# Sample output: 4 (3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(n)
def minNumberOfJumps(lst):
	jumps = [float("inf")] * len(lst)
	jumps[0] = 0

	for i in range(1, len(lst)):
		for j in range(i):
			if lst[j] + j >= i:
				jumps[i] = min(jumps[i], jumps[j] + 1)

	return jumps[-1]
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def minNumberOfJumps(lst):
	jumps = 0
	maxReach = lst[0]
	steps = lst[0]
	for i in range(1, len(lst)):
		maxReach = max(maxReach, lst[i] + i)
		steps -= 1
		if steps == 0:
			jumps += 1
			steps = maxReach - i
	return jumps + 1
# ----------------METHOD 02---------------------#
print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))