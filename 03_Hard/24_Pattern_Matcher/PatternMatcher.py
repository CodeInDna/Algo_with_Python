# --------------------------- PROBLEM 24 (HARD)-------------------------------#
# Pattern Matcher

# You are given two non-empty strings. The first one is a pattern consisting of only "x"s or "y"s; 
# the other one is a normal string of alphanumeric characters. 
# Write a function that checks whether or not the normal string matches the pattern. 
# A string S0 is said to match a pattern if replacing all "x"s in the pattern with some string S1 
# and replacing all "y"s in the pattern with some string S2 yields the same string S0. 
# If the input string does not match the input pattern, return an empty array; otherwise, 
# return an array holding the representations of "x" and "y" in the normal string, in that order. 
# If the pattern does not contain any "x"s or "y"s, the respective letter should be represented by an 
# empty string in the final array that you return. Assume that there will never be more than one pair of 
# strings S1 and S2 that appropriately represent "x" and "y" in the input string.

# Sample input: "xxyxxy", "gogopowerrangergogopowerranger"
# Sample output: ["go", "powerranger"]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2 + m), SPACE: O(n + m)
# n: length of pattern, m: length of string
def patternMatcher(pattern, string):
	if len(pattern) > len(string): return []

	newPattern = getNewPattern(pattern)
	didSwitch = newPattern[0] != pattern[0]

	counts = {'x': 0, 'y': 0}
	firstYPos = getCountAndFirstY(newPattern, counts)

	if counts["y"] != 0:
		for i in range(1, len(string)):
			len_x = i
			len_y = (len(string) - len_x * counts["x"]) / counts["y"]
			if len_y <= 0 or len_y % 1 != 0:
				continue
			len_y = int(len_y)
			yIdx = firstYPos * len_x
			x = string[:len_x]
			y = string[yIdx:yIdx + len_y]

			potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
			if string == "".join(potentialMatch):
				return [x, y] if not didSwitch else [y, x]
	else:
		len_x = len(string) / counts["x"]
		if len_x % 1 == 0:
			len_x = int(len_x)
			x = string[:len_x]
			potentialMatch = map(lambda char: x, newPattern)
			if string == "".join(potentialMatch):
				return [x, ""] if not didSwitch else ["", x]

	return []

def getCountAndFirstY(pattern, counts):
	firstYPos = None
	for i, char in enumerate(pattern):
		counts[char] += 1
		if char == 'y' and firstYPos is None:
			firstYPos = i
	return firstYPos

def getNewPattern(pattern):
	patternLetters = list(pattern)
	if pattern[0] == "x":
		return pattern
	return list(map(lambda char: "x" if char == "y" else "y", patternLetters))
# ----------------METHOD 01---------------------#
