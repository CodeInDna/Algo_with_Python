# ---------------------- PROBLEM 38 (RANDOM) ----------------------------------#
# Create Singly Linked List along with methods: push, traverse, pop, shift, unshift,
# insert, remove, get, set, reverse etc

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

	# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def shift(self):
		if not self.head: return None 

		currNode = self.head
		self.head = currNode.next

		self.length -= 1
		if self.length == 0: self.tail = None

		return currNode.val
	# ----------------METHOD 04---------------------#

	# ----------------METHOD 05---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def unshift(self, val):
		newNode = Node(val)
		if not self.head:
			self.head = newNode
			self.tail = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.length += 1
		return self
	# ----------------METHOD 05---------------------#

	# ----------------METHOD 06---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def get(self, idx):
		if idx < 0 or idx >= self.length: return None

		currNode = self.head
		count = 0 
		while count != idx:
			count += 1
			currNode = currNode.next
		return currNode
	# ----------------METHOD 06---------------------#

	# ----------------METHOD 07---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def set(self, idx, val):
		currNode = self.get(idx)
		if currNode:
			currNode.val = val
		return True
	# ----------------METHOD 07---------------------#

	# ----------------METHOD 08---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def insert(self, idx, val):
		if idx < 0 or idx > self.length:
			return False
		if idx == 0:
			return unshift(val)
		if idx == self.length:
			return push(val)

		newNode = Node(val)
		prevNode = self.get(idx - 1)
		newNode.next = prevNode.next
		prevNode.next = newNode
		self.length += 1

		return True
	# ----------------METHOD 08---------------------#

	# ----------------METHOD 09---------------------#
	# COMPLEXITY = BEST TIME: O(1), WORST TIME: O(n) SPACE: O(1)
	def remove(self, idx):
		if idx < 0 or idx >= self.length:
			return None
		if idx == 0:
			return self.shift()
		if idx == self.length-1:
			return self.pop()

		prevNode = self.get(idx - 1)
		removed = prevNode.next
		prevNode.next = removed.next
		self.length -= 1

		return removed
	# ----------------METHOD 09---------------------#

	# ----------------METHOD 10---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def reverse(self):
		currNode = self.head
		prevNode = None
		self.head, self.tail = self.tail, self.head
		while currNode is not None:
			nextNode = currNode.next
			currNode.next = prevNode
			prevNode = currNode
			currNode = nextNode
		return self
	# ----------------METHOD 10---------------------#

	# ----------------METHOD 11---------------------#
	# COMPLEXITY = TIME: O(n), SPACE: O(1)
	def rotate(self, pos):
		if pos < 1 or pos >= self.length: return None
		counter = 0
		while counter != pos:
			currNode = self.head
			nextNode = currNode.next
			self.head = nextNode
			currNode.next = None
			self.tail.next = currNode
			self.tail = currNode
			counter += 1
		return self
	# ----------------METHOD 11---------------------#