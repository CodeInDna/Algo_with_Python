# ---------------------------------- PROBLEM 02 (EASY) ----------------------------------------------#
# Find Closest Value in BST
# You are given a BST data structure consisting of BST nodes. Each BST node has an integer value 
# stored in a property called "value" and two children nodes stored in properties called "left" 
# and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST 
# property: its value is strictly greater than the values of every node to its left; its value 
# is less than or equal to the values of every node to its right; and both of its children nodes 
# are either BST nodes themselves or None (null) values. You are also given a target integer value; 
# write a function that finds the closest value to that target value contained in the BST. Assume 
# that there will only be one closest value.

# Sample Input:
#         10    ,12
#        /  \
#       5    15
#      / \   / \
#     2   5 13 22
#    /        \
#   1         14
# Sample Output: 13
# Assumption: 
	# * Input list : There will only be one closest value.

class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

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

bst = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22).insert(13).insert(14)

# ----------------METHOD 01---------------------#
# AVERAGE COMPLEXITY = TIME: O(log(n)), SPACE: O(1) 
# WORST COMPLEXITY = TIME: O(n), SPACE: O(1) 
def find_closest_value_in_bst(tree, target):
	closest = float("inf")
	currNode = tree
	while currNode:
		if abs(target - closest) > abs(target - currNode.value):
			closest = currNode.value
		if target > currNode.value:
			currNode = currNode.right
		elif target < currNode.value:
			currNode = currNode.left
		else:
			break
	return closest
print(find_closest_value_in_bst(bst, 12))
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# AVERAGE COMPLEXITY = TIME: O(log(n)), SPACE: O(log(n)) 
# WORST COMPLEXITY = TIME: O(n), SPACE: O(n) 
def find_closest_value_in_bst(tree, target):
	closest = float("inf")
	return bstHelper(tree, target, closest)

def bstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target > tree.value:
		return bstHelper(tree.right, target, closest)
	elif target < tree.value:
		return bstHelper(tree.left, target, closest)
	else:
		return closest
print(find_closest_value_in_bst(bst, 12))
# ----------------METHOD 02---------------------#


		
