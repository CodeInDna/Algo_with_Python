# ---------------------- PROBLEM 43 (RANDOM) ----------------------------------#
# # Create BST with two properties:
# 1. Each node in BST should not have more than 2 children
# 2. The nodes to the left of parent node should be smaller than the parent node and 
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

bst = BST()
bst.insert(10).insert(5).insert(2).insert(7).insert(13).insert(11).insert(16)
print(bst.root.val)
print(bst.root.left.val)
print(bst.root.left.left.val)
print(bst.root.left.right.val)
print(bst.root.right.val)
print(bst.root.right.left.val)
print(bst.root.right.right.val)