# ---------------------- PROBLEM 38 (RANDOM) ----------------------------------#
# Create Doubly Linked List along with methods: push, traverse, pop etc

class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

class DLL:
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
			newNode.prev = self.tail
			self.tail.next = newNode
			self.tail = newNode
		self.length += 1
		return self
	# ----------------METHOD 01---------------------#

	# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def traverse(self):
		if self.length <= 0: return None

		currNode = self.head
		while currNode is not None:
			print(currNode.val)
			currNode = currNode.next
	# ----------------METHOD 02---------------------#

	# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def pop(self):
		if self.head is None: return None

		poppedNode = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.tail = poppedNode.prev
			self.tail.next = None
			poppedNode.prev = None

		self.length -= 1 
		return poppedNode
	# ----------------METHOD 03---------------------#

	# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def shift(self):
		if self.head is None: return None

		shiftedNode = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = shiftedNode.next
			self.head.prev = None
			shiftedNode.next = None

		self.length -= 1 
		return shiftedNode
	# ----------------METHOD 04---------------------#

	# ----------------METHOD 05---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def unshift(self, val):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

		self.length += 1 
		return self
	# ----------------METHOD 05---------------------#
	