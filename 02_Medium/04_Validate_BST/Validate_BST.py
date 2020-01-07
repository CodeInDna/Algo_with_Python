# ---------------------------------- PROBLEM 4 (MEDIUM) --------------------------------------#
# Validate BST
# You are given a Binary Tree data structure consisting of Binary Tree nodes. Each Binary Tree 
# node has an integer value stored in a property called "value" and two children nodes stored 
# in properties called "left" and "right," respectively. Children nodes can either be Binary 
# Tree nodes themselves or the None (null) value. Write a function that returns a boolean representing 
# whether or not the Binary Tree is a valid BST. A node is said to be a BST node if and only if it 
# satisfies the BST property: its value is strictly greater than the values of every node to its left; 
# its value is less than or equal to the values of every node to its right; and both of its children 
# nodes are either BST nodes themselves or None (null) values.

# Sample Input:
# 		    10
# 		   /  \
#         5   15
#        /\   /\
#       2  5 13 22
#      /      \
#     1       14
# Sample Output : True

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
	
	# COMPLEXITY = TIME: O(n), SPACE: O(d) d: depth of the tree 
	def validateBST(tree):
		return BST.validateBSTHelper(tree, float("-inf"), float("inf"))
	
	def validateBSTHelper(tree, minvalue, maxvalue):
		if tree is None:
			return True
		if tree.value < minvalue or tree.value >= maxvalue:
			return False
		rightValidate = BST.validateBSTHelper(tree.right, tree.value, maxvalue)
		leftValidate = BST.validateBSTHelper(tree.left, minvalue, tree.value)
		return leftValidate and rightValidate

test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
.insert(13).insert(14)

print(BST.validateBST(test1))