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

# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(V log V+E), SPACE: O(V^2)
	def Dijkstra(self, start, finish):
		nodes = PriorityQueue()
		distances = {}
		previous = {}
		smallest = None
		path = []

		# build up initiale state
		for vertex in self.adjacencyList:
			if vertex == start:
				distances[vertex] = 0
				nodes.enqueue(vertex, 0)
			else: 
				distances[vertex] = float("inf")
				nodes.enqueue(vertex, float("inf"))
			previous[vertex] = None

		while len(nodes.values) != 0:
			smallest = nodes.dequeue()["val"]
			if smallest == finish:
				while smallest != None:
					path.append(smallest)
					smallest = previous[smallest]
				break

			for neigh in self.adjacencyList[smallest]:
				candidate = distances[smallest] + neigh["weight"]
				if candidate < distances[neigh["node"]]:
					distances[neigh["node"]] = candidate
					previous[neigh["node"]] = smallest
					nodes.enqueue(neigh["node"], candidate)
		return path[::-1]
# ----------------METHOD 03---------------------#


class PriorityQueue:
	def __init__(self):
		self.values = []

	def enqueue(self, val, priority):
		self.values.append({"val": val, "priority": priority})
		self.sort()
		return self.values

	def dequeue(self):
		return self.values.pop(0)

	def sort(self):
		self.values = sorted(self.values, key = lambda i: i['priority']) 



weightedGraph = WeightedGraph()
weightedGraph.addVertex("A")
weightedGraph.addVertex("B")
weightedGraph.addVertex("C")
weightedGraph.addVertex("D")
weightedGraph.addVertex("E")
weightedGraph.addVertex("F")
weightedGraph.addEdge("A", "B", 4)
weightedGraph.addEdge("A", "C", 2)
weightedGraph.addEdge("C", "D", 2)
weightedGraph.addEdge("C", "F", 4)
weightedGraph.addEdge("D", "E", 3)
weightedGraph.addEdge("D", "F", 1)
weightedGraph.addEdge("E", "F", 1)
weightedGraph.addEdge("E", "B", 3)

print(weightedGraph.Dijkstra("A", "E"))


