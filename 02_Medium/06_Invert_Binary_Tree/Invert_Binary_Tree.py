# ---------------------------------- PROBLEM 6 (MEDIUM) --------------------------------------#
# Invert Binary Tree
# Write a function that takes in a Binary Tree and inverts it. In other words, the function should 
# swap every left node in the tree for its corresponding (mirrored) right node. Each Binary Tree 
# node has a value stored in a property called "value" and two children nodes stored in properties 
# called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves 
# or the None (null) value.

# Sample Input:
# 		  1
# 		 / \
#        2  3
#       /\  /\
#      4  5 6 7
#     /\     
#    8  9    

# Sample Output:
# 		  1
# 		 / \
#        3  2
#       /\  /\
#      7  6 5 4
#    	   / \     
# 	       9 8  


# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def invertBinaryTree(tree):
	queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current is None:
			continue
		swapChildren(current)
		queue.append(current.left)
		queue.append(current.right)
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def invertBinaryTree(tree):
	if tree is None:
		return
	swapChildren(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
# ----------------METHOD 02---------------------#

def swapChildren(tree):
	tree.left, tree.right = tree.right, tree.left
