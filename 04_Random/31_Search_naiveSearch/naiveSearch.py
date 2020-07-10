# ---------------------- PROBLEM 31 (RANDOM) ----------------------------------#
# Write a function called naiveSearch which accepts two strings and returns the count
# of the short string present in the long ones.

# Sample input: wowomgzomg, omg
# Sample output: 2

# ----------------METHOD 01---------------------#
# COMPLEXITY = WORST/AVERAGE CASE TIME: O(n^2), BEST CASE TIME: O(n), SPACE: O(1)
def naiveSearch(string, pattern):
	count = 0

	for i in range(len(string)):
		j = 0
		while j < len(pattern):
			if pattern[j] != string[i + j]:
				break
			elif len(pattern)-1 == j:
				count += 1
			j += 1 
			
	return count
# ----------------METHOD 01---------------------#
print(naiveSearch('wowomgzomg', 'omg'))