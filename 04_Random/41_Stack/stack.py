# ---------------------- PROBLEM 41 (RANDOM) ----------------------------------#
# Create Stack functionality (LIFO i.e. Last In First Out)
# Examples: Function Call Stack (Recursion) | Undo/Redo | Browsing History
# We use two methods here: Linked List and List/Arrays(default functions).
# In Linked List method, we use shift(O(n)) and unshift(O(n)) methods for inserting and removing 
# elements instead of push(O(1)) and pop(O(n)) because of less time complexity.
# In array method, we will use push and pop because if we use shift and unshift
# all elements need to get reindexed which is not an optimal option to do.

# ----------------METHOD 01---------------------#
# USING LINKED LIST 
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Stack:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def push(self, val):
		newNode = Node(val)
		if self.first is None:
			self.first = newNode
			self.last = newNode
		else:
			newNode.next = self.first
			self.first = newNode
		self.size += 1
		return self

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def pop(self):
		if not self.first: return None 

		currNode = self.first
		self.first = currNode.next
		currNode.next = None

		self.size -= 1
		if self.size == 0: self.last = None

		return currNode

	def traverse(self):
		currentNode = self.first
		while currentNode is not None:
			print(currentNode.val)
			currentNode = currentNode.next

stck = Stack()
stck.push(1).push(2).push(3)
stck.traverse()
stck.pop()
stck.pop()
stck.pop()
stck.traverse()
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# USING PYTHON LIST/ARRAYS
# COMPLEXITY = TIME: O(1), SPACE: O(1)
stack = []
def push(element):
	stack.append(element)
	return stack

stack = push(1)
stack = push(2)
print(stack)
print(stack.pop())
print(stack)
# ----------------METHOD 02---------------------#