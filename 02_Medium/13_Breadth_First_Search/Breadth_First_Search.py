# ---------------------------------- PROBLEM 13 (MEDIUM) --------------------------------------#
# Breadth-first Search
# You are given a Node class that has a name and an array of optional children Nodes. When put 
# together, Nodes form a simple tree-like structure. Implement the breadthFirstSearch method on 
# the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search 
# approach (specifically navigating the tree from left to right), stores all of the Nodes' names in 
# the input array, and returns it.

# Sample Input:
# 		  A
#        /|\
#       B C D
#      /\   /\
#     E  F G  H
#       /\ \
#      I J  K
# Sample output: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(v + e), SPACE: O(v)
class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

	def addChild(self, value):
		self.children.append(Node(value))
		return self

	def breadthFirstSearch(self, array = []):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.value)
			for child in current.children:
				queue.append(child)
		return array
# ----------------METHOD 01---------------------#
