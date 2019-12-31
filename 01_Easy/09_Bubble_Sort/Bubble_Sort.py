# ---------------------------------- PROBLEM 09 (EASY) --------------------------------------#
# Bubble Sort
# Write a function that takes in array and returns a sorted array.
# USe buuble Sort to sort items.

# Sample input: [3, 1, 2]
# Sample output: [1, 2, 3]

# ----------------METHOD 01---------------------#
# BEST: COMPLEXITY = TIME: O(n), SPACE: O(1) 
# WORST/AVERAGE: COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
def bubbleSort(lst):
	for i in range(len(lst)-1, 0, -1):
		noSwaps = False
		for j in range(i):
			if lst[j] > lst[j+1]:
				lst = swap(j, j+1, lst)
				noSwaps = True
		if not noSwaps: return lst 
	return lst

def swap(idx1, idx2, lst):
	lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
	return lst
# ----------------METHOD 01---------------------#


# ----------------METHOD 02 (USING WHILE LOOP)---------------------#
# BEST: COMPLEXITY = TIME: O(n), SPACE: O(1) 
# WORST/AVERAGE: COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
def bubbleSort(lst):
	noSwaps = False
	counter = 0 
	while not noSwaps:
		noSwaps = True
		for i in range(len(lst) - 1 - counter):
			if lst[i] > lst[i+1]:
				swap(i, i+1, lst)
				noSwaps = False
		counter += 1
	return lst	
# ----------------METHOD 02---------------------#