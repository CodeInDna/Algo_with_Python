# ---------------------- PROBLEM 41 (RANDOM) ----------------------------------#
# Create Stack functionality (FIFO i.e. First In First Out)
# Examples: Queue of any kind | Background Tasks | Uploading Resources | Printing / Task Processing
# We use two methods here: Linked List and List/Arrays(default functions).
# In Linked List method, we use push(O(n)) and shift(O(n)) methods for inserting and removing 
# elements instead of unshift(O(1)) and pop(O(n)) because of less time complexity.
# In array method, we use either push and shift(O(1)) or unshift(O(1)) and pop but both 
# are not optimal method to use.

# ----------------METHOD 01---------------------#
# USING LINKED LIST 
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def enqueue(self, val):
		newNode = Node(val)
		if self.first is None:
			self.first = newNode
			self.last = newNode
		else:
			self.last.next = newNode
			self.last = newNode
		self.size += 1
		return self

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def dequeue(self):
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

queue = Queue()
queue.enqueue(1).enqueue(2).enqueue(3)
queue.traverse()
queue.dequeue()
queue.traverse()

# ----------------METHOD 02---------------------#
# USING PYTHON LIST/ARRAYS
# COMPLEXITY = TIME: O(n), SPACE: O(1)
queue = []
def enqueue(element):
	queue.append(element)
	return queue

def dequeue(queue):
	return queue.pop(0)

queue = enqueue(1)
queue = enqueue(2)
print(queue)
print(dequeue(queue))
print(queue)
# ----------------METHOD 02---------------------#