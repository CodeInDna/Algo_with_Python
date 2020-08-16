# ---------------------- PROBLEM 49 (RANDOM) ----------------------------------#
#

class WeightedGraph:
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
	def addEdge(self, vertex1, vertex2, weight):
		self.adjacencyList[vertex1].append({"node":vertex2, "weight": weight})
		self.adjacencyList[vertex2].append({"node":vertex1, "weight": weight})
		return self.adjacencyList
# ----------------METHOD 02---------------------#

class PriorityQueue:
	def __init__(self):
		self.values = []

	def enqueue(self, val, priority):
		self.values.append({"val": val, "priority": priority})
		self.sort()
		return self.values

	def dequeue(self):
		return self.pop(0)

	def sort(self):
		sorted(self.values, key = lambda x: x['priority']) 

weightedGraph = WeightedGraph()
weightedGraph.addVertex("A")
weightedGraph.addVertex("B")
weightedGraph.addVertex("C")
print(weightedGraph.addEdge("A", "B", 250))
print(weightedGraph.addEdge("C", "B", 30))

priority = PriorityQueue()
priority.enqueue("A", 2)
print(priority.enqueue("B", 1))