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

	def setHead(self, node):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		if self.head is None:
			self.head = node
			self.tail = node
			return self
		self.insertBefore(self.head, node)

	def setTail(self, node):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		if self.tail is None:
			self.setHead(node)
			return 
		self.insertAfter(self.tail, node)

	def containsNodeWithValue(self, value):
	# COMPLEXITY = TIME: O(n), SPACE: O(1) 
		currNode = self.head
		while currNode:
			if currNode.value == value:
				return True
			currNode = currNode.next
		return False

	def remove(self, node):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

	def removeNodeBindings(self, node):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None

	def removeNodesWithValue(self, value):
	# COMPLEXITY = TIME: O(n), SPACE: O(1) 
		currNode = self.head
		while currNode:
			nodeToRemove = currNode
			currNode = currNode.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
		return self

	def insertBefore(self, node, nodeToInsert):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		# Scenario 1: if nodeToInsert is the node which is the only node present in the linkedlist(head and tail)
		if self.head == nodeToInsert and self.tail == nodeToInsert:
			return
		# Scenario 2: If nodeToInsert is already in the linkedlist, then first remove it from the DLL and then insert it before the node given
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	def insertAfter(self, node, nodeToInsert):
	# COMPLEXITY = TIME: O(1), SPACE: O(1) 
		# Scenario 1: if nodeToInsert is the node which is the only node present in the linkedlist(head and tail)
		if self.head == nodeToInsert and self.tail == nodeToInsert:
			return
		# Scenario 2: If nodeToInsert is already in the linkedlist, then first remove it from the DLL and then insert it after the node given
		self.remove(nodeToInsert)
		nodeToInsert.next = node.next
		nodeToInsert.prev = node
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	def insertAtPosition(self, position, nodeToInsert):
	# COMPLEXITY = TIME: O(p), SPACE: O(1) 
		# Scenario 1: if the position is 1 then make it head
		if position == 1:
			self.setHead(nodeToInsert)
			return
		# Scenario 2: Iterate over the linked list to find the position where in we have to insert the node
		currNode = self.head
		count = 1 
		while currNode and count != position:
			currNode = currNode.next
			if currNode is None:
				# Scenario 3: if the position is last then make it a tail
				self.setTail(nodeToInsert)
			else:
				self.insertBefore(currNode, nodeToInsert)
			count += 1

				 
dll = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
dll.setHead(first)
dll.insertBefore(first, second)
dll.insertBefore(second, third)
dll.insertBefore(third, fourth)
dll.insertBefore(fourth, fifth)
dll.insertBefore(fourth, sixth)
dll.insertAtPosition(2, seventh)
node = dll.head
while node:
	print(node.value)
	node = node.next
# ----------------METHOD 01---------------------#


