# ---------------------- PROBLEM 45 (RANDOM) ----------------------------------#
# 

class Graph:
	def __init__(self):
		self.adjacencyList = {}

# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def addVertex(self, vertex_name):
		if vertex_name not in self.adjacencyList:
			self.adjacencyList[vertex_name] = []
		return self.adjacencyList
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def addEdge(self, vertex1, vertex2):
		self.adjacencyList[vertex1].append(vertex2)
		self.adjacencyList[vertex2].append(vertex1)
		return self.adjacencyList
# ----------------METHOD 02---------------------#

graph = Graph()
print(graph.addVertex('A'))
print(graph.addVertex('B'))
print(graph.addEdge('B','A'))