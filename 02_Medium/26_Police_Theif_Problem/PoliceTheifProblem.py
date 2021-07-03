# --------------------------- PROBLEM 25 (HARD)-------------------------------#
# Given an array of size n that has the following specifications: 

# Each element in the array contains either a policeman or a thief.
# Each policeman can catch only one thief.
# A policeman cannot catch a thief who is more than K units away from the policeman.
# We need to find the maximum number of thieves that can be caught.
# Examples: 
 

# Input : arr[] = {'P', 'T', 'T', 'P', 'T'},
#             k = 1.
# Output : 2.
# Here maximum 2 thieves can be caught, first
# policeman catches first thief and second police-
# man can catch either second or third thief.

# Input : arr[] = {'T', 'T', 'P', 'P', 'T', 'P'}, 
#             k = 2.
# Output : 3.

# Input : arr[] = {'P', 'T', 'P', 'T', 'T', 'P'},
#             k = 3.
# Output : 3.

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def catch_the_theif(arr, k):
	police = [idx for idx, ele in enumerate(arr) if ele == 'P']
	theif = [idx for idx, ele in enumerate(arr) if ele == 'T']

	p = 0
	t = 0
	theif_caught = 0
	while(p < len(police) and t < len(theif)):
		if abs(police[p] - theif[t] <= k):
			theif_caught += 1
			p += 1
			t += 1
		elif theif[t] < police[p]:
			t += 1
		else:
			p += 1
	return theif_caught
# ----------------METHOD 01---------------------#
