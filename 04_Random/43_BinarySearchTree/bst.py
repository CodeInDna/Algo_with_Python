# ---------------------- PROBLEM 43 (RANDOM) ----------------------------------#
# # Create BST with two properties:
# 1. Each node in BST should not have more than 2 children
# 2. The nodes to the left of the parent node should be smaller than the parent node and 
# nodes right to the parent node should be larger than the parent node.


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

# ----------------METHOD 01---------------------#
	# COMPLEXITY = BEST/AVERAGE TIME: O(logn), WORST TIME: O(n), SPACE: O(1)
	def insert(self, val):
		newNode = Node(val)
		if self.root is None:
			self.root = newNode
			return self

		currNode = self.root

		while True:
			if newNode.val > currNode.val:
				if currNode.right:
					currNode = currNode.right
				else:
					currNode.right = newNode
					return self
			else:
				if currNode.left:
					currNode = currNode.left
				else:
					currNode.left = newNode
					return self
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = BEST/AVERAGE TIME: O(logn), WORST TIME: O(n), SPACE: O(1)
	def find(self, target):
		if self.root is None:
			return False

		currNode = self.root

		while currNode is not None:
			if currNode.val == target:
				return True
			elif target > currNode.val:
				currNode = currNode.right
			else:
				currNode = currNode.left
		return False 
# ----------------METHOD 02---------------------#


# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(V + E), SPACE: O(V), V-number of vertices, E-number of edges
	def bfs(self):
		node = self.root
		data = []
		queue = []
		queue.append(node)
		while len(queue):
			node = queue.pop(0)
			data.append(node.val)
			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)
		return data
# ----------------METHOD 03---------------------#

# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(V + E), SPACE: O(V), V-number of vertices, E-number of edges
	def dfs_preorder(self):
		result = []
		node = self.root

		def dfs_helper(result, node):
			result.append(node.val)
			if node.left: dfs_helper(result, node.left)
			if node.right: dfs_helper(result, node.right)
		dfs_helper(result, node)
		return result
# ----------------METHOD 04---------------------#

# ----------------METHOD 05---------------------#
	# COMPLEXITY = TIME: O(V + E), SPACE: O(V), V-number of vertices, E-number of edges
	def dfs_postorder(self):
		result = []
		node = self.root

		def dfs_helper(result, node):
			if node.left: dfs_helper(result, node.left)
			if node.right: dfs_helper(result, node.right)
			result.append(node.val)
		dfs_helper(result, node)
		return result
# ----------------METHOD 05---------------------#

# ----------------METHOD 05---------------------#
	# COMPLEXITY = TIME: O(V + E), SPACE: O(V), V-number of vertices, E-number of edges
	def dfs_inorder(self):
		result = []
		node = self.root

		def dfs_helper(result, node):
			if node.left: dfs_helper(result, node.left)
			result.append(node.val)
			if node.right: dfs_helper(result, node.right)
		dfs_helper(result, node)
		return result
# ----------------METHOD 05---------------------#

bst = BST()
bst.insert(10).insert(5).insert(2).insert(7).insert(13).insert(11).insert(16)
print(bst.root.val)
print(bst.root.left.val)
print(bst.root.left.left.val)
print(bst.root.left.right.val)
print(bst.root.right.val)
print(bst.root.right.left.val)
print(bst.root.right.right.val)


print(bst.find(11))
print(bst.find(12))
print(bst.find(10))

print(bst.bfs())
print(bst.dfs_preorder())
print(bst.dfs_postorder())
print(bst.dfs_inorder())