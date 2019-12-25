# ---------------------------------- PROBLEM 03 (EASY) ----------------------------------------------#
# Depth First Search
# You are Tree class that has a name and an array of optional cTrees. When put 
# toTrees form a simple tree-like structure. Implement the depthFirstSearch method onTree class, which takes in an empty array, traverses the tree using the Depth-first Search 
# approach (specifically navigating the tree from left to right), stores all theTrees' 
# names in the input array, and returns it.
# Sample input:
# 		  A
#        /|\
#       B C D
#      /\   /\
#     E  F G  H
#       /\ \
#      I  J K
# Sample output: ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

class Tree:
	def __init__(self, value):
		self.value = value
		self.children = []

	def addChild(self, value):
		child = Tree(value)
		self.children.append(child)
		return self

	# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(v + e), SPACE: O(v) 
	def depth_first_search(self, array):
		array.append(self.value)
		for child in self.children:
			child.depth_first_search(array)
		return array
	# ----------------METHOD 01---------------------#

test1 = Tree("A")
test1.addChild("B").addChild("C").addChild("D")
test1.children[0].addChild('E').addChild('F')
test1.children[0].children[1].addChild('I').addChild('J')

test1.children[2].addChild('G').addChild('H')
test1.children[2].children[0].addChild('K')

print(test1.depth_first_search([]))


# print(test1.children[0].children)
# for child in test1.children[2].children[0].children:
# 	print(child.value)

