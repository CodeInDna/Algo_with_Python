# ---------------------------------- PROBLEM 11 (MEDIUM) --------------------------------------#
# Levenshtein Distance
# Write a function that takes in two strings and returns the minimum number of edit operations that 
# need to be performed on the first string to obtain the second string. There are three edit operations: 
# insertion of a character, deletion of a character, and substitution of a character for another.

# Sample input: "abc", "yabd"
# Sample output: 2 (insert "y"; substitute "c" for "d")

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(nm), SPACE: O(nm), n:num_of_rows, m:num_of_cols 
def levenshteinDistance(str1, str2):
	# edits = [[x for x in range(len(str2)+1)] for y in range(len(str1) + 1)]
	# for i in range(len(str1)+1):
	# 	edits[i][0] = i
	edits = [[x for x in range(y, len(str2)+y+1)] for y in range(len(str1) + 1)]
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
				edits[i][j] = edits[i-1][j-1]
			else:
				edits[i][j] = 1 + min(edits[i-1][j-1], edits[i][j-1], edits[i-1][j])
	return edits[-1][-1]
# ----------------METHOD 01---------------------#
