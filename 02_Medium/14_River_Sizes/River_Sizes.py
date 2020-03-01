# ---------------------------------- PROBLEM 13 (MEDIUM) --------------------------------------#
# River Sizes
# You are given a two-dimensional array (matrix) of potentially unequal height and width containing 
# only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of 
# any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). 
# The number of adjacent 1s forming a river determine its size. Write a function that returns an array 
# of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be 
# in any particular order.

# Sample input:
# [
#    [1, 0, 0, 1, 0],
#    [1, 0, 1, 0, 0],
#    [0, 0, 1, 0, 1],
#    [1, 0, 1, 0, 1],
#    [1, 0, 1, 1, 0],
# ]
# Sample Output: [1,2,2,2,5]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(wh) or O(N), SPACE: O(wh) w:width, h:height
def riverSizes(matrix):
	sizes = []
	has_visited = [[False for value in row] for row in matrix]
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if has_visited[row][col]:
				continue
			traverseNode(row, col, matrix, has_visited, sizes)
	return sorted(sizes)

def traverseNode(i, j, matrix, has_visited, sizes):
	currentRiverSize = 0
	nodesToExplore = [[i, j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]

		# if the node visited, continue
		if has_visited[i][j]:
			continue
		# if not visited, set as visited
		has_visited[i][j] = True	
		# if the node is land, continue
		if matrix[i][j] == 0: 		# piece of land
			continue
		# node is river 
		currentRiverSize += 1
		# get all unvisited neighbors
		univisitedNeighbours = getUnvisitedNeighbors(i, j, matrix, has_visited)
		for neighbors in univisitedNeighbours:
			nodesToExplore.append(neighbors)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
	unvisited = []
	if i > 0 and not visited[i - 1][j]:
		unvisited.append([i - 1, j])

	if i < len(matrix)-1 and not visited[i + 1][j]:
		unvisited.append([i + 1, j])

	if j > 0 and not visited[i][j - 1]:
		unvisited.append([i, j - 1])

	if j < len(matrix[0])-1 and not visited[i][j + 1]:
		unvisited.append([i, j + 1])
	return unvisited

print(riverSizes([
   [1, 0, 0, 1, 0],
   [1, 0, 1, 0, 0],
   [0, 0, 1, 0, 1],
   [1, 0, 1, 0, 1],
   [1, 0, 1, 1, 0],
]))
# ----------------METHOD 01---------------------#
