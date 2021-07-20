# ---------------------------------- PROBLEM 20 (MEDIUM) --------------------------------------#
# Search In Sorted Matrix

# You are given a two-dimensional array (matrix) of distinct integers where each row is sorted and 
# each column is also sorted. The matrix does not necessarily have the same height and width. You 
# are also given a target number, and you must write a function that returns an array of the row 
# and column indices of the target number if it is contained in the matrix and [-1, -1] if it is not 
# contained in the matrix.

# Sample input:
# [
#  [1, 4, 7, 12, 15, 1000],
#  [2, 5, 19, 31, 32, 1001],
#  [3, 8, 24, 33, 35, 1002],
#  [40, 41, 42, 44, 45, 1003],
#  [99, 100, 103, 106, 128, 1004],
# ], 44
# Sample Output: [3,3]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def searchInSortedMatrix(matrix, target):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == target:
				return [i, j]
	return [-1, -1]
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(log(n)), SPACE: O(1) 
def search(arr, target):
	# Using Divide and Conquer On an array
	# Define left and right
	left = 0
	right = len(arr) - 1

	# loop until result found
	while left <= right:
		mid = (left + right) // 2
		print(left, right, mid, target)
		# Find the mid
		if arr[mid] == target:
			return mid
		elif target < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return -1

def searchInSortedMatrix(matrix, target):
	# iterate over the rows
	for idx_r, row in enumerate(matrix):
		# search the target in each row
		col_idx = search(row, target)
		if col_idx != -1:
			# return the arr if column is not -1
			return [idx_r, col_idx]
	return [-1, -1]
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n + m) n:length of rows, m:length of the column, SPACE: O(1)
def searchInSortedMatrix(matrix, target):
	row = 0
	column = len(matrix[row]) - 1
	while row < len(matrix) and column >= 0:
		if matrix[row][column] > target:
			column -= 1
		elif matrix[row][column] < target:
			row += 1
		else:
			return [row, column]
	return [-1, -1]
# ----------------METHOD 03---------------------#