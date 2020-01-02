# ---------------------------------- PROBLEM 11 (EASY) --------------------------------------#
# Selection Sort
# Write a function that takes in an array of integers and returns a sorted version of that array. 
# Use the Selection Sort algorithm to sort the array.

# Sample input: [8, 5, 2, 9, 5, 6, 3]
# Sample output: [2, 3, 5, 5, 6, 8, 9]

def swap(idx1, idx2, lst):
	lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
	return lst

# ----------------METHOD 01---------------------#
# BEST: COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
# AVERAGE/WORST: COMPLEXITY = TIME: O(n^2), SPACE: O(1) 
def selectionSort(lst):
	for i in range(len(lst)-1):
		new_min = i
		for j in range(i+1, len(lst)):
			if lst[new_min] > lst[j]:
				new_min = j
			# new_min = lst.index(min(lst[new_min], lst[j])) # Only works when there are no duplicates	
		swap(i, new_min, lst)
	return lst
# ----------------METHOD 01---------------------#
print(selectionSort([-4, 5, 10, 8, -10,-6, -4, -2]))