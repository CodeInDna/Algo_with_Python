# ---------------------------------- PROBLEM 3 (MEDIUM) --------------------------------------#
# BST Construction
# Write a Binary contains Tree (BST) class. The class should have a "value" property set to be an 
# integer, as well as "left" and "right" properties, both of which should point to either the 
# None (null) value or to another BST. A node is said to be a BST node if and only if it satisfies 
# the BST property: its value is strictly greater than the values of every node to its left; its 
# value is less than or equal to the values of every node to its right; and both of its children 
# nodes are either BST nodes themselves or None (null) values. The BST class should support 
# insertion, containsing, and removal of values. The removal method should only remove the first 
# instance of the target value.

# Sample Input:
# 	      10
# 	      /\
#        5  15
#        /\ /\
#       2 5 13 22
#      /     \
#     1      14
# Sample Output (after inserting 12):
# 		   10
# 		  /  \
#        5    15
#        /\   /\
#       2  5 13 22
#      /     /\
#     1    12 14
# Sample Output (after removing 10):
# 		    12
# 		   / \
#         5  15
#        /\  /\
#       2 5 13 22
#      /     \
#     1      14
# Sample output (after containsing for 15): True

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# ----------------INSERT METHOD 01---------------------#
	# RECURSIVE INSERTION
	# AVERAGE/BEST COMPLEXITY = TIME: O(log(n)), SPACE: O(log(n))
	# WORST COMPLEXITY = TIME: O(n), SPACE: O(n): If BST is one sided
	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self
# ----------------INSERT METHOD 01---------------------#

# ----------------INSERT METHOD 02---------------------#
	# AVERAGE/BEST COMPLEXITY = TIME: O(log(n)), SPACE: O(1)
	# WORST COMPLEXITY = TIME: O(n), SPACE: O(1): If BST is one sided
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
# ----------------INSERT METHOD 02---------------------#

# ----------------SEARCH METHOD 01---------------------#
	# RECURSIVE SEARCHING
	# AVERAGE/BEST COMPLEXITY = TIME: O(log(n)), SPACE: O(log(n))
	# WORST COMPLEXITY = TIME: O(n), SPACE: O(n): If BST is one sided
	def contains(self, target):
		if target == self.value:
			return True
		elif target < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(target)
		elif target > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(target)
		else:
			return False
# ----------------SEARCH METHOD 01---------------------#

# ----------------SEARCH METHOD 02---------------------#
	# AVERAGE/BEST COMPLEXITY = TIME: O(1), SPACE: O(log(n))
	# WORST COMPLEXITY = TIME: O(n), SPACE: O(1): If BST is one sided
	def contains(self, target):
		currNode = self
		while currNode:
			if target < currNode.value:
				currNode = currNode.left
			elif target > currNode.value:
				currNode = currNode.right
			else:
				return True
		return False
# ----------------SEARCH METHOD 02---------------------#

	def remove(self, target, parentNode=None):
		# Step 1: Find the node
		currNode = self
		while currNode:
			if target > currNode.value:
				parentNode = currNode
				currNode = currNode.right
			elif target < currNode.value:
				parentNode = currNode
				currNode = currNode.left
			else:
				# Step 2: If number is found, define edge cases
				# CASE 1: If Node has two children
				if currNode.left is not None and currNode.right is not None:
					currNode.value = currNode.right.getMinValue()
					currNode.right.remove(currNode.value, currNode)
				# CASE 2: If Node is the root node of BST and has only one or no child
				elif parentNode is None:
					if currNode.left is not None:
						currNode.value = currNode.left.value
						currNode.right = currNode.left.right
						currNode.left = currNode.left.left
					elif currNode.right is not None:
						currNode.value = currNode.right.value
						currNode.left = currNode.right.left
						currNode.right = currNode.right.right
					else:
						currNode.value = None
				# CASE 3: If Node has parent and the node is on the left of parent node
				elif parentNode.left == currNode:
					parentNode.left = currNode.left if currNode.left is not None else currNode.right
				# CASE 3: If Node has parent and the node is on the right of parent node
				elif parentNode.right == currNode:
					parentNode.right = currNode.left if currNode.left is not None else currNode.right
				break
		return self
		
	def getMinValue(self):
		currNode = self
		while currNode.left:
			currNode = currNode.left
		return currNode.value

