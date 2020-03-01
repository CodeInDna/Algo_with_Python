# ---------------------------------- PROBLEM 15 (MEDIUM) --------------------------------------#
# Youngest Common Ancestor

# You're given three inputs, all of which are instances of a class that have an "ancestor" property 
# pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., 
# the only instance that has no ancestor), and the other two inputs are descendants in the ancestral 
# tree. Write a function that returns the youngest common ancestor to the two descendants.

# Sample input: Node A, Node E, Node I (from the ancestral tree below)
#      A
#     / \
#    B   C
#    /\  /\
#   D  E F G
#  /\
# H  I
# Sample Output: Node B

# COMPLEXITY = TIME: O(d), SPACE: O(1), d: depth
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendentDepth(descendantOne, topAncestor)
	depthTwo = getDescendentDepth(descendantTwo, topAncestor)

	if depthOne > depthTwo:
		return backTrackAncestoralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backTrackAncestoralTree(descendantTwo, descendantOne, depthTwo - depthOne)
	
def getDescendentDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backTrackAncestoralTree(lowerDescendent, higherDescendent, diff):
	while diff > 0:
		lowerDescendent = lowerDescendent.ancestor
		diff -= 1
	while lowerDescendent != higherDescendent:
		lowerDescendent = lowerDescendent.ancestor
		higherDescendent = higherDescendent.ancestor
	return lowerDescendent

