# --------------------------- PROBLEM 25 (HARD)-------------------------------#
# Multi String Search

# Write a function that takes in a "big" string and an array of "small" strings, all of which are smaller in length than 
# the big string. The function should return an array of booleans, where each boolean represents whether or not the small
#  string at that index in the array of small strings is contained in the big string. Note that you cannot use language-built
# -in string-matching methods.

# Sample input: "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
# Sample output: [True, False, True, True, False, True, False]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(bn), SPACE: O(n)
# b : Length of big string
# n : Length of array of small string
def multiStringSearch(bigString, arrSmallStr):
	return [searchWord(bigString, smallString) for smallString in arrSmallStr]

def searchWord(bigStr, smallStr):
	for idx in range(len(bigStr)):
		if bigStr[idx:idx + len(smallStr)] == smallStr:
			return True
	return False 
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(bns), SPACE: O(n)
# b : Length of big string
# n : Length of array of small string
# s : Length of array of biggest small string
def multiStringSearch(bigString, arrSmallStr):
	return [searchWord(bigString, smallString) for smallString in arrSmallStr]
	
def searchWord(bigStr, smallStr):
	for startIdx in range(len(bigStr)-len(smallStr)+1):
		if inBigString(bigStr, smallStr, startIdx):
			return True
	return False

def inBigString(bigStr, smallStr, startIdx):
	leftBigIdx = startIdx
	rightBigIdx = startIdx + len(smallStr) - 1
	leftSmallIdx = 0 
	rightSmallIdx = len(smallStr) - 1

	while(leftBigIdx <= rightBigIdx):
		if bigStr[leftBigIdx] != smallStr[leftSmallIdx]:
			return False
		leftBigIdx += 1
		leftSmallIdx += 1

	return True
# ----------------METHOD 02---------------------#
