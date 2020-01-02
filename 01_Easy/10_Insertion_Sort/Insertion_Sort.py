# ---------------------------------- PROBLEM 10 (EASY) --------------------------------------#
# Insertion Sort
# Write a function that takes in an array of integers and returns a sorted version of that array. 
# Use the Insertion Sort algorithm to sort the array.

# Sample input: [8, 5, 2, 9, 5, 6, 3]
# Sample output: [2, 3, 5, 5, 6, 8, 9]

def swap(idx1, idx2, lst):
	lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
	return lst

# ----------------METHOD 01---------------------#
# BEST: COMPLEXITY = TIME: O(n), SPACE: O(1) 
# AVERAGE/WORST: COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
def insertionSort(lst):
	for i in range(1, len(lst)):
		j = i
		while j > 0 and lst[j] < lst[j-1]:
			swap(j, j-1, lst)
			j-=1
	return lst
# ----------------METHOD 01---------------------#