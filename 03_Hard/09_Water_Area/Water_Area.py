# ---------------------------------- PROBLEM 9 (HARD)--------------------------------------#
# Water Area

# You are given an array of integers. Each non-zero integer represents the height of a pillar 
# of width 1. Imagine water being poured over all of the pillars and return the surface area of 
# the water trapped between the pillars viewed from the front. Note that spilled water should be 
# ignored. Refer to the first minute of the video explanation below for a visual example.

# Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
# Sample output: 48


# ----------------METHOD 01 (a)---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def waterArea(heights):
	leftMax = [0] * len(heights)
	rightMax = [0] * len(heights)
	waterTrapped = [None] * len(heights)

	for i in range(1, len(heights)):
		leftMax[i] = max(heights[i - 1], leftMax[i - 1])

	for j in range(len(heights) - 2, -1, -1):
		rightMax[j] = max(heights[j + 1], rightMax[j + 1])
	
	for k in range(len(heights)):
		minHeight = min(leftMax[k], rightMax[k])
		if heights[k] < minHeight:
			waterTrapped[k] = minHeight - heights[k]
		else:
			waterTrapped[k] = 0
	return sum(waterTrapped)
# ----------------METHOD 01 (a)---------------------#

# ----------------METHOD 01 (b)---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def waterArea(heights):
	leftMax = 0
	rightMax = 0
	waterTrapped = [0] * len(heights)

	for i in range(1, len(heights)):
		leftHeight = heights[i - 1]
		leftMax = max(leftMax, leftHeight)
		waterTrapped[i] = leftMax

	for j in reversed(range(len(heights))):
		height = heights[j]
		minHeight = min(waterTrapped[j], rightMax)

		if heights[j] < minHeight:
			waterTrapped[j] = minHeight - height
		else:
			waterTrapped[j] = 0
		rightMax = max(rightMax, height)

	return sum(waterTrapped)
# ----------------METHOD 01 (b)---------------------#