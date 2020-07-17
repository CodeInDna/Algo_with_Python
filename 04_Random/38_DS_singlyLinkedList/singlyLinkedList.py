# ---------------------- PROBLEM 38 (RANDOM) ----------------------------------#
# Create Singly Linked List along with methods: push, traverse, pop etc

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(n)
	def push(self, val):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
		self.length += 1
		return self
	# ----------------METHOD 01---------------------#

	# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def traverse(self):
		currNode = self.head
		while currNode:
			print(currNode.val)
			currNode = currNode.next
	# ----------------METHOD 02---------------------#

	# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def pop(self):
		if not self.head: return None

		currNode = self.head
		prevNode = currNode
		while currNode.next is not None:
			prevNode = currNode	
			currNode = currNode.next

		self.length -= 1
		if self.length == 0: self.head = None; self.tail = None

		self.tail = prevNode
		prevNode.next = None
		return currNode.val 
	# ----------------METHOD 03---------------------#

sll_1 = SLL().push(1).push(2).push(3)

sll_1.traverse()
sll_1.pop()
sll_1.pop()
sll_1.pop()
sll_1.traverse()