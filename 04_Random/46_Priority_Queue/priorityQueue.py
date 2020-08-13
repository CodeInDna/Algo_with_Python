# ---------------------- PROBLEM 46 (RANDOM) ----------------------------------#
# Create Priority Queue using heaps.
# E.g. Patients with different priority levels comes in hospital and need to be served 
# according to the severity of their symptoms. For instance 
# patient who encountered a major accident need to look after first before the 
# patient with a mild headache.
# So here we need to create a heap according to the priority level. The highest 
# priority thing should come first and so on.

class Node:
	def __init__(self, val, priority):
		self.val = val
		self.priority = priority

class PriorityQueue:
	def __init__(self):
		self.values = []


# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(logn), SPACE: O(1)
	def enqueue(self, val, priority):
		newNode = Node(val, priority)
		self.values.append(newNode)
		self.bubbleUp()
		return [(node.priority, node.val) for node in self.values]

	def bubbleUp(self):
		queue = self.values
		idx = len(self.values) - 1
		parent_idx = (idx-1) // 2

		while queue[parent_idx].priority > queue[idx].priority and idx > 0 :
			queue[parent_idx], queue[idx] = queue[idx], queue[parent_idx]
			idx = parent_idx
			parent_idx = (idx-1) // 2
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(logn), SPACE: O(1)
	def dequeue(self):
		queue_len = len(self.values) - 1
		self.values[0], self.values[queue_len] = self.values[queue_len], self.values[0]
		popped_node = self.values.pop(queue_len)
		if queue_len > 0 :
			self.bubbleDown()
		return (popped_node.priority, popped_node.val)

	def bubbleDown(self):
		queue = self.values
		parent_idx = 0
		priority = queue[parent_idx].priority
		length = len(self.values)

		while True:
			swap = None
			left_child_idx = 2 * parent_idx + 1
			right_child_idx = 2 * parent_idx + 2

			if left_child_idx < length:
				if queue[left_child_idx].priority < priority:
					swap = left_child_idx

			if right_child_idx < length:
				if ((queue[right_child_idx].priority < priority) 
					and (queue[right_child_idx].priority < queue[left_child_idx].priority)):
					swap = right_child_idx

			if swap is None: break

			queue[swap], queue[parent_idx] = queue[parent_idx], queue[swap]

			parent_idx = swap 
# ----------------METHOD 02---------------------#

queue = PriorityQueue()
print(queue.enqueue("sick", 3))     # [(3, 'sick')] 
print(queue.enqueue("accident", 2))	# [(2, 'accident'), (3, 'sick')]
print(queue.enqueue("severe operation", 1))	# [(1, 'severe operation'), (3, 'sick'), (2, 'accident')]

print(queue.dequeue())	# (1, 'severe operation')
print(queue.dequeue())	# (2, 'accident')
print(queue.dequeue())	# (3, 'sick')
print(queue.values)		# []