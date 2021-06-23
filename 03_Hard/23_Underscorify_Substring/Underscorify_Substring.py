# --------------------------- PROBLEM 23 (HARD)-------------------------------#
# Underscorify Substring

# Write a function that takes in two strings: a main string and a potential substring of the main string. 
# The function should return a version of the main string with every instance of the substring in it wrapped 
# between underscores. 
# If two instances of the substring in the main string overlap each other or sit side by side, 
# the underscores relevant to these two substrings should only appear on the far left of the left substring 
# and on the far right of the right substring. If the main string does not contain the other string at all, r
# eturn the main string intact.

# Sample input: "testthis is a testtest to see if testestest it works", "test"
# Sample output: "_test_this is a _testtest_ to see if _testestest_ it works"

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(a), SPACE: O(a)
def underscorifySubstring(string, substring):
	locations = collapseLocations(getLocations(string, substring))

	if not len(locations):
		return string

	return underscorify(string, locations)

# COMPLEXITY = TIME: O(a), SPACE: O(a)
# a: Number of matches(substring) in the main string
def getLocations(string, substring):
	locations = []
	startIdx = 0

	while(startIdx < len(string)):
		nextIdx = string.find(substring, startIdx)
		if nextIdx != -1:
			locations.append([nextIdx, nextIdx + len(substring)])
			startIdx = nextIdx + 1
		else:
			break

	return locations

# COMPLEXITY = TIME: O(a), SPACE: O(a-b)
# a: Number of matches(substring) in the main string
# b: Number of collapse locations
def collapseLocations(locations):
	if not len(locations):
		return locations 

	newLocations = [locations[0]]
	prevLoc = newLocations[0]

	for i in range(1, len(locations)):
		currLoc = locations[i]
		if currLoc[0] <= prevLoc[1]:
			prevLoc[1] = currLoc[1]
		else:
			newLocations.append(currLoc)
			prevLoc = currLoc
	return newLocations

# COMPLEXITY = TIME: O(a), SPACE: O(1)
# a: Number of matches(substring) in the main string
def underscorify(string, locations):
	start_idx = 0
	end_idx = locations[0][0]
	new_string = ''
	for loc in locations:
		end_idx = loc[0]
		new_string += string[start_idx:end_idx]
		new_string += '_'
		start_idx = loc[0]
		end_idx = loc[1]
		new_string += string[start_idx:end_idx]
		new_string += '_'
		start_idx = end_idx
	new_string += string[end_idx:]
	return new_string
# ----------------METHOD 01---------------------#