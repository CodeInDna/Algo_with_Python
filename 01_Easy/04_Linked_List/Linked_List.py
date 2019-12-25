# ---------------------------------- PROBLEM 04 (EASY) ----------------------------------------------#
# Linked List Construction
# Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, 
# both of which should point to either the None (null) value or to a Linked List node. Every 
# node will have a "value" property as well as "next" and "prev" properties, both of which can 
# point to either the None (null) value or another node. The class should support setting the 
# head and tail of the linked list, inserting nodes before and after other nodes as well as at 
# certain positions, removing given nodes and removing nodes with specific values, and searching 
# for nodes with values. Only the searching method should return a value: specifically, a boolean.

# Sample Input:
# 1 -> 2 -> 3 -> 4 -> 5
# Sample output (after setting 4 to head):
# 4 -> 1 -> 2 -> 3 -> 5
# Sample output (after setting 6 to tail):
# 4 -> 1 -> 2 -> 3 -> 5 -> 6
# Sample output (after inserting a new 3 after 6):
# 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
# Sample output (after inserting a new 3 at position 1):
# 3 -> 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
# Sample output (after removing nodes with value 3):
# 4 -> 1 -> 2 -> 5 -> 6
# Sample output (after removing 2):
# 4 -> 1 -> 5 -> 6
# Sample output (after searching for 5): True


# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(), SPACE: O() 
class Node:

	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

class DoublyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def setHead(self, value):
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			currNode = self.head
			currNode.prev = newNode
			self.head = newNode
			self.head.next = currNode
		return self

	def setTail(self, value):
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			currNode = self.tail
			currNode.next = newNode
			self.tail = newNode
			self.tail.prev = currNode
		return self

	def containsNodeWithValue(self, value):
		currNode = self.head
		while currNode:
			if currNode.value == value:
				return True
			currNode = currNode.next
		return False

	def removeNodes(self, value):
		currNode = self.head
		

dll = DoublyLinkedList()
dll.setHead(2)
dll.setHead(1)
dll.setTail(3)
print(dll.containsNodeWithValue(1))
# dll.setHead(1)
# print(dll.tail.value)
# print(dll.head.value)
# print(dll.head.next.value)
# ----------------METHOD 01---------------------#


