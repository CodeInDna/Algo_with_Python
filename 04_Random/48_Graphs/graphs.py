# ---------------------- PROBLEM 45 (RANDOM) ----------------------------------#
# A Graph is a non-linear data structure consisting of nodes and edges. 
# The nodes are sometimes also referred to as vertices and the edges are lines or 
# arcs that connect any two nodes in the graph.
# USES: Social Networks, Location/ Mapping, Routing Algos, Visual Hierarchy, File System Oraganizations.
class Graph:
	def __init__(self):
		self.adjacencyList = {}

# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(|V| + |E|)
	def addVertex(self, vertex_name):
		if vertex_name not in self.adjacencyList:
			self.adjacencyList[vertex_name] = []
		return self.adjacencyList
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(|V| + |E|)
	def addEdge(self, vertex1, vertex2):
		self.adjacencyList[vertex1].append(vertex2)
		self.adjacencyList[vertex2].append(vertex1)
		return self.adjacencyList
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(E), SPACE: O(1)
	def removeEdge(self, vertex1, vertex2):
		self.adjacencyList[vertex1].remove(vertex2)
		self.adjacencyList[vertex2].remove(vertex1)
		return self.adjacencyList
# ----------------METHOD 03---------------------#

# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(|V| + |E|), SPACE: O(1)
	def removeVertex(self, vertex2):
		lst = self.adjacencyList[vertex2].copy()
		for vertex1 in lst:
			self.removeEdge(vertex1, vertex2)
		del self.adjacencyList[vertex2]
		return self.adjacencyList
# ----------------METHOD 04---------------------#

graph = Graph()
graph.addVertex('Tokyo')
graph.addVertex('Dallas')
graph.addVertex('Aspen')
graph.addVertex('Hong Kong')
graph.addVertex('Los Angeles')
graph.addEdge('Hong Kong','Tokyo')
graph.addEdge('Aspen','Dallas')
graph.addEdge('Los Angeles','Dallas')
graph.addEdge('Hong Kong','Dallas')
graph.addEdge('Dallas','Tokyo')
print(graph.addEdge('Los Angeles','Hong Kong'))
# {'Tokyo': ['Hong Kong', 'Dallas'], 
# 'Dallas': ['Aspen', 'Los Angeles', 'Hong Kong', 'Tokyo'], 
# 'Aspen': ['Dallas'], 
# 'Hong Kong': ['Tokyo', 'Dallas', 'Los Angeles'], 
# 'Los Angeles': ['Dallas', 'Hong Kong']}

# print(graph.removeEdge('Hong Kong','Dallas'))
print(graph.removeVertex("Hong Kong"))
# {'Tokyo': ['Dallas'], 
# 'Dallas': ['Aspen', 'Los Angeles', 'Tokyo'], 
# 'Aspen': ['Dallas'], 'Los Angeles': ['Dallas']}