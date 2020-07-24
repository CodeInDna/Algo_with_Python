# ---------------------- PROBLEM 38 (RANDOM) ----------------------------------#
# Create Doubly Linked List along with methods: push, traverse, pop, shift, unshift,
# insert, remove, get, set, reverse etc

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

	# ----------------METHOD 06---------------------#
	# COMPLEXITY = WORST/AVERAGE TIME: O(n/2) or O(n), BEST TIME: O(1), SPACE: O(1)
	def get(self, idx):
		if idx < 0 or idx >= self.length: return None

		if idx <= self.length//2:
			currNode = self.head
			counter = 0
			while counter != idx:
				currNode = currNode.next
				counter += 1
		else:
			currNode = self.tail
			counter = self.length-1
			while counter != idx:
				currNode = currNode.prev
				counter -= 1
		return currNode
 	# ----------------METHOD 06---------------------#

 	# ----------------METHOD 07---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def set(self, idx, val):
		node = self.get(idx)
		if node:
			node.val = val
			return True
		return False
 	# ----------------METHOD 07---------------------#

 	# ----------------METHOD 08---------------------#
	# COMPLEXITY = BEST TIME: O(1), WORST/AVERAGE TIME: O(n) or O(n/2), SPACE: O(1)
# 1.If pointer is given in this case Time Complexity is O(1).
# 2.You DON'T have pointer to the node to be deleted(Search and Insert). 
# In this case Time Complexity is O(n).
	def insert(self, idx, val):
		if idx < 0 or idx > self.length: return False

		if idx == 0: return self.unshift(val)
		if idx == self.length: return self.push(val)

		newNode = Node(val)
		prevNode = self.get(idx-1)
		currNext = prevNode.next
		prevNode.next = newNode
		newNode.prev = prevNode
		newNode.next = currNext
		currNext.prev = newNode

		self.length += 1
		return True
 	# ----------------METHOD 08---------------------#

 	# ----------------METHOD 09---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
# 1.If pointer is given in this case Time Complexity is O(1).
# 2.You DON'T have pointer to the node to be deleted(Search and Delete). 
# In this case Time Complexity is O(n).
	def remove(self, idx):
		if idx < 0 or idx >= self.length: return False
		if idx == 0: return self.shift()
		if idx == self.length-1: return self.pop()

		removedNode = self.get(idx) # TIME COMPLEXITY: n or n/2
		prevNode = removedNode.prev
		nextNode = removedNode.next
		prevNode.next, nextNode.prev = nextNode, prevNode
		removedNode.next, removedNode.prev = None, None

		self.length -= 1
		return removedNode
 	# ----------------METHOD 09---------------------#


 	# ----------------METHOD 10---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def reverse(self):
		currNode = self.head
		self.head, self.tail = self.tail, self.head
		while currNode is not None:
			prevNode = currNode.prev
			nextNode = currNode.next
			currNode.next, currNode.prev = prevNode, nextNode
			currNode = nextNode
		return self

 	# ----------------METHOD 10---------------------#

