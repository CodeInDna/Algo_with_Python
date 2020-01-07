# ---------------------------------- PROBLEM 5 (MEDIUM) --------------------------------------#
# BST Traversal
# You are given a BST data structure consisting of BST nodes. Each BST node has an integer value 
# stored in a property called "value" and two children nodes stored in properties called "left" 
# and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST 
# property: its value is strictly greater than the values of every node to its left; its value 
# is less than or equal to the values of every node to its right; and both of its children nodes 
# are either BST nodes themselves or None (null) values. Write three functions that take in an empty 
# array, traverse the BST, add its nodes' values to the input array, and return that array. The three 
# functions should traverse the BST using the in-order traversal, pre-order traversal, and post-order 
# traversal techniques, respectively.

# Sample Input:
# 			10
# 			/\
#          5  15
#         /\   \
#        2  5  22
#       /     
#      1      
# Sample output (inOrderTraverse): [1, 2, 5, 5, 10, 15, 22]
# Sample output (preOrderTraverse): [10, 5, 2, 1, 5, 15, 22]
# Sample output (postOrderTraverse): [1, 2, 5, 5, 22, 15, 10]

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
		currNode = self
		while True:
			if value < currNode.value:
				if currNode.left is None:
					currNode.left = BST(value)
					break
				else:
					currNode = currNode.left
			else:
				if currNode.right is None:
					currNode.right = BST(value)
					break
				else:
					currNode = currNode.right
		return self
	
	# COMPLEXITY = TIME: O(n), SPACE: O(n) 
	def inOrderTraverse(tree, array = []):
		if tree is not None:
			BST.inOrderTraverse(tree.left, array)
			array.append(tree.value)
			BST.inOrderTraverse(tree.right, array)
		return array

	# COMPLEXITY = TIME: O(n), SPACE: O(n) 
	def preOrderTraverse(tree, array = []):
		if tree is not None:
			array.append(tree.value)
			BST.preOrderTraverse(tree.left, array)
			BST.preOrderTraverse(tree.right, array)
		return array

	# COMPLEXITY = TIME: O(n), SPACE: O(n) 
	def postOrderTraverse(tree, array = []):
		if tree is not None:
			BST.postOrderTraverse(tree.left, array)
			BST.postOrderTraverse(tree.right, array)
			array.append(tree.value)
		return array

test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
.insert(13).insert(14)

print(BST.inOrderTraverse(test1))
print(BST.preOrderTraverse(test1))
print(BST.postOrderTraverse(test1))