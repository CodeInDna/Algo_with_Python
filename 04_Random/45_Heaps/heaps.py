# ---------------------- PROBLEM 45 (RANDOM) ----------------------------------#

class BinaryHeap:
	def __init__(self):
		self.values = []

# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(logn), SPACE: O(1)
	def maxHeapInsert(self, val):
		self.values.append(val)
		self.bubbleUp()
		return self.values
		
	def bubbleUp(self):
		idx = len(self.values) - 1
		parent = (idx-1) // 2

		while self.values[parent] < self.values[idx] and idx > 0:
			self.values[parent], self.values[idx] = self.values[idx], self.values[parent]
			idx = parent
			parent = (idx-1) // 2
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(logn), SPACE: O(1)
	def maxHeapRemove(self):
		self.values[0], self.values[len(self.values)-1] = self.values[len(self.values)-1], self.values[0]
		popped_node = self.values.pop(len(self.values)-1)
		self.bubbleDown()
		return self.values	

	def bubbleDown(self):
		node = self.values
		parent_idx = 0
		element = node[parent_idx]
		length = len(self.values)

		while True:
			swap = None
			left_child_idx = 2 * parent_idx + 1
			right_child_idx = 2 * parent_idx + 2

			if left_child_idx < length:
				if node[left_child_idx] > element:
					swap = left_child_idx

			if right_child_idx < length:
				if node[right_child_idx] > element and node[right_child_idx] > node[left_child_idx]:
					swap = right_child_idx

			if swap == None: break
			
			node[swap], node[parent_idx] = node[parent_idx], node[swap]

			parent_idx = swap
# ----------------METHOD 02---------------------#

maxHeap = BinaryHeap()
maxHeap.maxHeapInsert(100)
maxHeap.maxHeapInsert(19)
maxHeap.maxHeapInsert(40)
maxHeap.maxHeapInsert(7)
maxHeap.maxHeapInsert(15)
maxHeap.maxHeapInsert(26)
print(maxHeap.maxHeapInsert(32))
print(maxHeap.maxHeapRemove())